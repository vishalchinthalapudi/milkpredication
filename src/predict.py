import joblib
import pandas as pd

def predict(sample):
    model = joblib.load("model/model.pkl")
    sample = pd.DataFrame([sample])
    return model.predict(sample)[0]
