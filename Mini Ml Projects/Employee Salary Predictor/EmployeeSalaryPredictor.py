# for handling data frame from data set ot table or files
import pandas as pd

# for handling array
import numpy as np

# In this I'm going to find the employee salary by years of exp. so it's numaric finding so 
# I'm going to use linear regression 
from sklearn.linear_model import LinearRegression

# used to spilt the full data into test and train
from sklearn.model_selection import train_test_split

# used to measure how good the model is here we are using regression model we we can't use accrucy score here
from sklearn.metrics import r2_score, mean_absolute_error

import matplotlib.pyplot as plt

# data loaded
df = pd.read_csv("Mini Ml Projects/Employee Salary Predictor/Salary_data.csv")


# data cleaing started

# find the count of null values in each coulmn
print(df.isnull().sum())

# 2. Force conversion to numeric (this turns empty strings/text into actual NaN)
df['YearsExperience'] = pd.to_numeric(df['YearsExperience'], errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# drop null values we need to store the altered file to again orginal df
# because pandas not modify the original df it'll return the new df we need 
# get and store another df
print(f"count before droped the null coulmns : {df.count()}\n")
# df = df.dropna()
df.dropna(axis=0, how='any', subset=['YearsExperience', 'Salary'], inplace=True)
# df.dropna(how='any', inplace=True)
print(f"count after droped the null coulmns : {df.count()}\n")
# here we are find the average years of experience to fill empty or null or nan places
# df["YearsExperience"] = df["YearsExperience"].fillna(df["YearsExperience"].mean())

# same for salary column
# df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# remove the duplicate rows
print(f"duplicate count : \n{df.duplicated().sum()}\n")
df.drop_duplicates()


# spilt the test and train data
X = df[["YearsExperience"]] # here X is the our input data based on this years experiece 
Y = df[["Salary"]] # here Y is the our output data result this is the salary will be this years experiece

# now we are going to spilt the our data set into two part for testing and training
# test_size -  usealy the test data will be 20% so we used test_size = 0.2 and train will be rest now (80%).
# random_state - this should be anything but we should be mention any number mostly all are using 42
X_train, X_test, y_train, y_test = train_test_split(
    X,Y,test_size=0.2,random_state=42
)

# here we are choosing LinearRegression as our algoritham to make that model to learn the patterns from X,Y train using fit mothod
model = LinearRegression()
model.fit(X_train,y_train)

# just check the model is got the patterens
# my tesing with random numbers
testing_df = pd.DataFrame({
    "YearsExperience" : [1,3]
})
testing_predict = model.predict(testing_df)

print(f"testing_predict \n{testing_predict}")

# predict with X_test data from our data set
y_pred = model.predict(X_test)

# Step 8: Check score using r2_score because we are using regression model
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"R2 Score (Model Accuracy): {r2:.2f}\n")
print(f"Average Error in Salary: ${mae:.2f}\n")

# Step 9: Compare actual vs predicted
# print("Actual values:", y_test)
# print("Predicted values:", y_pred)

# Plot the real data points
plt.scatter(X_test, y_test, color='red', label='Actual')

# Plot the regression line
plt.plot(X_test, y_pred, color='blue', linewidth=2, label='Predicted')

above_15_years = pd.DataFrame({
    "YearsExperience": [15,16,17,18,19,20]
})

stress_predict =model.predict(above_15_years)

print(f"stress_predict \n {stress_predict}\n")

plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

# print(df)