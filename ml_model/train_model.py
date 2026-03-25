import joblib
from sklearn.ensemble import RandomForestClassifier

# Dummy training data
X = [
    [10,2,1],
    [2,0,0],
    [15,5,2],
    [1,0,0]
]

y = [1,0,1,0]  # 1 = attack, 0 = normal

model = RandomForestClassifier()
model.fit(X,y)

joblib.dump(model,"ml_model/model.pkl")

print("Model trained and saved")