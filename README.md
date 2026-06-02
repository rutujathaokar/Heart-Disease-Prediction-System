# ❤️ Heart Disease Prediction System

A Machine Learning based web application that predicts the likelihood of heart disease using patient health parameters. The system uses a trained Random Forest model and provides real-time predictions through a Flask web interface.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help individuals seek timely medical attention.

This project uses Machine Learning techniques to analyze medical attributes and predict whether a patient has a high or low chance of heart disease.

---

## 🚀 Features

- Real-time heart disease prediction
- User-friendly web interface
- Probability-based prediction
- Machine Learning powered backend
- Flask web application
- Input validation and preprocessing
- Fast and accurate predictions

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- NumPy
- Pickle

---

## 📂 Project Structure

```text
CVD/
│
├── static/
│   ├── bg_img.jpeg
│   └── collegelogo.jpeg
│
├── templates/
│   └── index.html
│
├── all_models(1).pkl
├── app.py
├── check_accuracy.py
├── heart.csv
```

---

## 📊 Dataset

The project uses a heart disease dataset containing the following medical parameters:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope of ST Segment
- Number of Major Vessels
- Thalassemia

---

## 🤖 Machine Learning Models

Multiple machine learning algorithms were evaluated during development:

- Random Forest
- Support Vector Machine (SVM)
- Decision Tree
- Logistic Regression
- K-Nearest Neighbors (KNN)

After comparing performance, **Random Forest** achieved the highest accuracy and was selected for deployment.

---

## 🌳 Why Random Forest?

Random Forest was chosen because:

- High prediction accuracy
- Reduced overfitting
- Works well with structured medical datasets
- Uses multiple decision trees for better generalization
- Provides robust and reliable predictions

---

## ⚙️ Working Flow

1. User enters medical details through the web form.
2. Flask receives the input data.
3. Data preprocessing converts categorical values into numerical format.
4. The trained Random Forest model is loaded from the `.pkl` file.
5. Prediction is generated.
6. Result and prediction probability are displayed to the user.

---

## 📈 Prediction Output

The application provides:

- High Chance of Heart Disease
- Low Chance of Heart Disease
- Prediction Probability (%)

---

## 🧠 Model Deployment

The trained machine learning model is stored in:

```text
all_models(1).pkl
```

The Flask backend loads this model during runtime and performs real-time predictions.

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/rutujathaokar/Heart-Disease-Prediction-System.git
cd heart-disease-prediction
```

### Install Dependencies

```bash
pip install flask numpy scikit-learn pandas
```

### Run Application

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

## 📚 Literature Insights

During literature review, several research papers using Random Forest, SVM, Ensemble Learning, and Hybrid Models were analyzed. Based on comparative studies and experimental evaluation, Random Forest was selected due to its superior performance and reliability for heart disease prediction.

---

## 🔮 Future Scope

- Larger healthcare datasets
- Integration with hospital management systems
- Cloud deployment
- Explainable AI (XAI)
- Patient report generation
- Mobile application support

---

## 👩‍💻 Authors

- Rutuja Thaokar
- ## Contributors
- Prachita Wandile

## 📄 License

This project is developed for educational and academic purposes.
