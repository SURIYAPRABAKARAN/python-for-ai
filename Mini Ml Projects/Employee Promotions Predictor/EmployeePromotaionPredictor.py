import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt

df = pd.read_csv("Mini Ml Projects/Employee Promotions Predictor/employee_promotions.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Feature Engineering
df['is_senior'] = (df['experience'] >= 10).astype(int)
df['high_performer'] = (df['performance_score'] >= 8).astype(int)
df['good_attendance'] = (df['attendance'] >= 85).astype(int)
df['salary_level'] = df['salary'] // 10000

# Encoding
df = pd.get_dummies(df, columns=['gender', 'department'], drop_first=True)

# Features and target
X = df.drop("promoted", axis=1)
y = df["promoted"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# df['promoted'].value_counts().plot(kind='bar')
# plt.scatter(df['experience'], df['promoted'])
plt.scatter(df['salary'], df['promoted'])
plt.title("Promotion Count")
plt.xlabel("Promoted")
plt.ylabel("Number of Employees")
plt.show()

# cm = confusion_matrix(y_test, y_pred)
# print(cm)
# plt.imshow(cm)
# plt.title("Confusion Matrix")
# plt.xlabel("Predicted")
# plt.ylabel("Actual")

# for i in range(len(cm)):
#     for j in range(len(cm)):
#         plt.text(j, i, cm[i][j])

# plt.show()

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
