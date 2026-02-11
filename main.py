from src.data_load import load_data
from src.preprocessing import preprocess
from src.model import train_model
from src.visualization import plot_ph

data = load_data("data/milknew.csv")
data = preprocess(data)

plot_ph(data)

model = train_model(data)

print("Training Completed")
