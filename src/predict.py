import joblib
import pandas as pd

def predict(sample):
    model = joblib.load("outputs/model.pkl")
    sample = pd.DataFrame([sample])
    result = model.predict(sample)
    return result
