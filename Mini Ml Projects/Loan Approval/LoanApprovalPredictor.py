import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

# encode ( words / test into 0,1 because machine know only 0s and 1s )
from sklearn.preprocessing import LabelEncoder

# used to measure how good the model is
from sklearn.metrics import accuracy_score

# graff
import matplotlib.pyplot as plt

# data loaded
df = pd.read_csv("Mini Ml Projects/Loan Approval/loan_data.csv")

# there is no empty or none fields so data is correct
# print(df.isna().sum())

# feture engineering new columns are not needed.

# data preprocessing
le_gender = LabelEncoder()
le_edu = LabelEncoder()
le_home = LabelEncoder()
le_intent = LabelEncoder()
le_default = LabelEncoder()

df["person_gender"] = le_gender.fit_transform(df["person_gender"])
df["person_education"] = le_edu.fit_transform(df["person_education"])
df["person_home_ownership"] = le_home.fit_transform(df["person_home_ownership"])
df["loan_intent"] = le_intent.fit_transform(df["loan_intent"])
df["previous_loan_defaults_on_file"] = le_default.fit_transform(df["previous_loan_defaults_on_file"])

# spilt the data test and train
X = df[["person_age","person_gender","person_education","person_income","person_emp_exp","person_home_ownership","loan_amnt","loan_intent","loan_int_rate","loan_percent_income","cb_person_cred_hist_length","credit_score","previous_loan_defaults_on_file"]]
Y = df["loan_status"]

X_train , X_test , y_train, y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42
)

# model = ExtraTreeClassifier() accuracy score -  0.8686666666666667


model = DecisionTreeClassifier() # accuracy score -  0.9007777777777778 so I used DecisionTreeClassifier


model.fit(X_train,y_train)

sample_data = pd.DataFrame({
    "person_age": [22.0],
    "person_gender": le_gender.transform(["female"]),
    "person_education": le_edu.transform(["Master"]),
    "person_income": [71948.0],
    "person_emp_exp": [0],
    "person_home_ownership": le_home.transform(["RENT"]),
    "loan_amnt": [35000.0],
    "loan_intent": le_intent.transform(["PERSONAL"]),
    "loan_int_rate": [16.02],
    "loan_percent_income": [0.49],
    "cb_person_cred_hist_length": [3.0],
    "credit_score": [561],
    "previous_loan_defaults_on_file": le_default.transform(["No"])
})

# output = model.predict(sample_data)

# print(output)

# predict
y_predict = model.predict(X_test)

accuracy = accuracy_score(y_test,y_predict)

print(accuracy)
