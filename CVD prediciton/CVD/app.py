import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

try:
    # to print all the models
    with open('all_models(1).pkl', 'rb') as f:
        loaded_list = pickle.load(f)

    print("Type of loaded_list:", type(loaded_list))
    print("Length of list:", len(loaded_list))

    for i, item in enumerate(loaded_list):
        print(f"Model {i}:", type(item))

    model = loaded_list[0]  # using first model
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Function to preprocess the form data
# Converts user input → model format
def preprocess_input(data):
    # Convert categorical variables to numerical
    chest_pain_mapping = {'typical_angina': 0, 'atypical_angina': 1, 'non_anginal_pain': 2, 'asymptomatic': 3}
    sex_mapping = {'male': 1, 'female': 0}
    yes_no_mapping = {'yes': 1, 'no': 0} #fasting blood sugar
    ecg_mapping = {'normal': 0, 'st_t_abnormality': 1, 'left_ventricular_hypertrophy': 2}
    slope_mapping = {'upsloping': 0, 'flat': 1, 'downsloping': 2}
    thal_mapping = {'normal': 1, 'fixed_defect': 2, 'reversible_defect': 3}

    data['sex'] = sex_mapping[data['sex']]
    data['chest_pain_type'] = chest_pain_mapping[data['chest_pain_type']]
    data['fasting_blood_sugar'] = yes_no_mapping[data['fasting_blood_sugar']]
    data['resting_ecg'] = ecg_mapping[data['resting_ecg']]
    data['exercise_induced_angina'] = yes_no_mapping[data['exercise_induced_angina']]
    data['slope'] = slope_mapping[data['slope']]
    data['thal'] = thal_mapping[data['thal']]

    # Must match training dataset
    features = [data['age'], data['sex'], data['chest_pain_type'], 
                data['resting_bp'], data['cholesterol'], data['fasting_blood_sugar'],
                data['resting_ecg'], data['max_heart_rate'], data['exercise_induced_angina'],
                data['st_depression'], data['slope'], data['num_vessels'], data['thal']]

    # reshape it into a 2D array as required by the model
    return np.array(features).reshape(1, -1)

@app.route('/')
def home():
    return render_template('index.html')

# Triggered when user clicks Submit button
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collects all input values from HTML
        form_data = {
            'age': int(request.form['age']),
            'sex': request.form['sex'].lower(),
            'chest_pain_type': request.form['chest_pain_type'],
            'resting_bp': int(request.form['resting_bp']),
            'cholesterol': int(request.form['cholesterol']),
            'fasting_blood_sugar': request.form['fasting_blood_sugar'],
            'resting_ecg': request.form['resting_ecg'],
            'max_heart_rate': int(request.form['max_heart_rate']),
            'exercise_induced_angina': request.form['exercise_induced_angina'],
            'st_depression': float(request.form['st_depression']),
            'slope': request.form['slope'],
            'num_vessels': int(request.form['num_vessels']),
            'thal': request.form['thal']
        }

        # Preprocess input
        features = preprocess_input(form_data)

        # Make prediction
        # predict() for classification and predict_proba() to show probability percentage.
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)[0][1] * 100  # Get probability of heart disease

        # Format prediction probability to 1 decimal place
        prediction_proba = round(prediction_proba, 1)

        # Create prediction message
        has_disease = "High Chance of Heart Disease" if prediction[0] == 1 else "Low Chance of Heart Disease"

        # Display data and prediction
        display_data = {
            'age': form_data['age'],
            'gender': 'Male' if form_data['sex'] == 'male' else 'Female',
            'chest_pain_types': {'typical_angina': 'Typical Angina', 'atypical_angina': 'Atypical Angina', 
                                 'non_anginal_pain': 'Non-Anginal Pain', 'asymptomatic': 'Asymptomatic'}[request.form['chest_pain_type']],
            'resting_blood_pressure': form_data['resting_bp'],
            'cholesterol_level': form_data['cholesterol'],
            'is_fasting_blood_pressure_greater_than_120mg_dl': 'Yes' if form_data['fasting_blood_sugar'] == 'yes' else 'No',
            'resting_ecg_result': {'normal': 'Normal', 'st_t_abnormality': 'ST-T Wave Abnormality',
                                   'left_ventricular_hypertrophy': 'Left Ventricular Hypertrophy'}[request.form['resting_ecg']],
            'maximum_heart_rate': form_data['max_heart_rate'],
            'exercise_induced_angina': 'Yes' if form_data['exercise_induced_angina'] == 'yes' else 'No',
            'st_depression': form_data['st_depression'],
            'slope_of_st_segment': {'upsloping': 'Upsloping', 'flat': 'Flat', 'downsloping': 'Downsloping'}[request.form['slope']],
            'num_vessels': form_data['num_vessels'],
            'thal_type': {'normal': 'Normal', 'fixed_defect': 'Fixed Defect', 'reversible_defect': 'Reversible Defect'}[request.form['thal']]
        }

        return render_template('index.html', 
                               prediction=has_disease, 
                               probability=prediction_proba,
                               data=display_data,
                               show_result=True)

    except Exception as e:
        return render_template('index.html', error=f"Error making prediction: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
    
    