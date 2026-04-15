from sklearn.linear_model import LogisticRegression
import pickle


# Sample data
# x [age,salary]
X = [[22, 20000], [25, 25000], [47, 50000], [52, 60000]]
y = [0, 0, 1, 1]  # 0 = No, 1 = Yes

model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
    
print("Model saved as model.pkl")