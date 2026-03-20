import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("Mini Ml Projects/Student Grade Predictor/students_datas_for_validation.csv")

# Step 1: Create Grade column
def getGradeByMark(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 50:
        return "C"
    else:
        return "Fail"

df["Grade"] = df["Marks"].apply(getGradeByMark)

X = df[["Marks"]]
y = df["Grade"]

model = DecisionTreeClassifier()

model.fit(X, y)

new_data = pd.DataFrame({
    "Marks": [49, 51, 78, 98]
})

prediction = model.predict(new_data)

print(prediction)

print(df)