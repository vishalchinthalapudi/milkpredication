import seaborn as sns
import matplotlib.pyplot as plt

def plot_ph(data):
    sns.countplot(x='pH', data=data)
    plt.title("pH Distribution")
    plt.show()

def plot_temperature(data):
    sns.countplot(x='Temperature', data=data)
    plt.title("Temperature Distribution")
    plt.show()
