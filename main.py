import os
from src.data_load import load_data
from src.preprocessing import preprocess
from src.train import train_model

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "data", "milknew.csv")

data = load_data(data_path)
data = preprocess(data)

train_model(data)

print("Model trained and saved successfully ✅")
