# for data handling making data frame
import pandas as pd
# for working with array
import numpy as np

# model with classifier type
from sklearn.tree  import DecisionTreeClassifier

from sklearn.model_selection import train_test_split

# used to measure how good the model is
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

# data has been readed from CSV converted into data frame
df =  pd.read_csv("Mini Ml Projects/Student Result Predictor/StudentMarks.csv")

# data cleaning

# df = df.dropna()

df.isna().sum() # sum == 0

# df.drop_duplicates()

# spilt test and train data
X = df[["Maths", "Physics", "Chemistry"]]
Y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42
)

# model going to understand the patterns
# pattern is all the subject mark should be >= 35
model = DecisionTreeClassifier()

model.fit(X_train,y_train)

just_check = pd.DataFrame({
    "Maths": [36],
    "Physics": [34],
    "Chemistry": [36]
})


# Step 7: Predict using test data
y_pred = model.predict(X_test)

print(model.predict(just_check))


# Step 8: Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
# Plot the regression line
X_test["Average"] = (X_test["Maths"] + X_test["Physics"] + X_test["Chemistry"]) / 3

plt.scatter(X_test["Average"], y_test)
plt.xlabel("Average Marks")
plt.ylabel("Result")
plt.title("Average vs Result")
plt.show()