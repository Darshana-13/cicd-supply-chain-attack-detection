import joblib

model = joblib.load("ml_model/model.pkl")

def predict_attack(features):

    results = []

    for feature in features:
        prediction = model.predict([feature])

        if prediction[0] == 1:
            results.append("attack")
        else:
            results.append("safe")

    return results