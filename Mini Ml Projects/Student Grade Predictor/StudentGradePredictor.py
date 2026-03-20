# pandas is used for handling data (like tables)
import pandas as pd

# DecisionTreeClassifier is used for classification problems
# It learns patterns and predicts categories (A, B, C, Fail)
from sklearn.tree import DecisionTreeClassifier

# used to split data into training and testing
from sklearn.model_selection import train_test_split

# used to measure how good the model is
from sklearn.metrics import accuracy_score

import numpy as np

# set seed for reproducibility
np.random.seed(42)

names = [
    "Suriya","Arun","Kumar","Rahul","Krish","Priya","Anil","Vijay","Meena",
    "Ravi","Sneha","Karthik","Divya","Ajay","Nisha","Ramesh","Pooja","Manoj",
    "Keerthi","Arvind","Lakshmi","Santhosh","Deepa","Hari"
]

data = []

for i in range(200):
    name = np.random.choice(names) + str(i)   # make unique names
    age = np.random.randint(20, 31)           # age between 20–30
    marks = np.random.randint(30, 101)        # marks between 30–100
    
    data.append([name, age, marks])

# create dataframe
df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])

# save to CSV
df.to_csv("Mini Ml Projects/Student Grade Predictor/students_large_dataset.csv", index=False)

print("Dataset created successfully!")
print(df.head())


# Step 1: Load dataset
df = pd.read_csv("Mini Ml Projects/Student Grade Predictor/students_large_dataset.csv")


# Step 2: Feature Engineering
# Create Grade column based on Marks
def getGradeByMark(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

# Apply function to create new column
df["Grade"] = df["Marks"].apply(getGradeByMark)


# Step 3: Prepare data
# X = input (Marks)
# y = output (Grade)
X = df[["Marks"]]
y = df["Grade"]


# Step 4: Split data into training and testing
# 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 5: Create model
model = DecisionTreeClassifier()


# Step 6: Train model using training data
model.fit(X_train, y_train)


# Step 7: Predict using test data
y_pred = model.predict(X_test)


# Step 8: Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)


# Step 9: Compare actual vs predicted
print("Actual values:", y_test.values)
print("Predicted values:", y_pred)


# Step 10: Test with new data
new_data = pd.DataFrame({
    "Marks": [49, 51, 78, 98]
})

prediction = model.predict(new_data)

print("New Predictions:", prediction)


# Step 11: Show full dataset
print("\nFinal Dataset:")
print(df)