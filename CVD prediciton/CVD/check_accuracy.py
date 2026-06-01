import pickle
import pandas as pd
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("heart.csv")

X = data.drop("target", axis=1)
y = data["target"]

# Load models
with open("all_models(1).pkl", "rb") as f:
    models = pickle.load(f)

# Model names (for clarity)
model_names = [
    "Random Forest",
    "Logistic Regression",
    "KNN",
    "SVM",
    "Decision Tree"
]

# Check accuracy for each model
for i, model in enumerate(models):
    y_pred = model.predict(X)
    acc = accuracy_score(y, y_pred)
    print(f"{model_names[i]} Accuracy: {round(acc * 100, 2)}%")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

















# Random forest code
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# import pickle

# # 1. Load dataset
# data = pd.read_csv('heart.csv')

# # 2. Split into features (X) and target (y)
# X = data.drop('target', axis=1)   # input features
# y = data['target']                # output (0 or 1)

# # 3. Split into training and testing data
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # 4. Create Random Forest model
# model = RandomForestClassifier(
#     n_estimators=100,   # number of trees
#     random_state=42
# )

# # 5. Train the model
# model.fit(X_train, y_train)

# # 6. Test the model
# y_pred = model.predict(X_test)

# # 7. Check accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# # 8. Save the model as .pkl file
# with open('all_models(1).pkl', 'wb') as f:
#     pickle.dump([model], f)