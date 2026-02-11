from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model(data):

    X = data.drop('Grade', axis=1)
    y = data['Grade']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)
    joblib.dump(model, "outputs/model.pkl")

    return model
