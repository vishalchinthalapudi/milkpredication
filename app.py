import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Milk Quality Predictor", page_icon="🥛")

st.title("🥛 Milk Quality Prediction using CSV File")
st.write("Upload a CSV file and download predicted results")

# Load model
@st.cache_resource
def load_model():
    return joblib.load(os.path.join("model", "model.pkl"))

model = load_model()

# Upload file
uploaded_file = st.file_uploader("Upload Milk Dataset CSV", type=["csv"])

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(data.head())

    # Ensure required columns
    required_columns = ["pH","Temperature","Taste","Odor","Fat","Turbidity","Colour"]

    if all(col in data.columns for col in required_columns):

        X = data[required_columns]

        predictions = model.predict(X)

        mapping = {0:"Low",1:"Medium",2:"High"}
        data["Predicted_Grade"] = [mapping[p] for p in predictions]

        st.subheader("Prediction Results")
        st.dataframe(data.head())

        # Convert to CSV
        csv = data.to_csv(index=False).encode('utf-8')

        st.download_button(
            label="📥 Download Predicted CSV",
            data=csv,
            file_name="milk_predictions.csv",
            mime="text/csv"
        )

    else:
        st.error("CSV must contain columns: pH, Temperature, Taste, Odor, Fat, Turbidity, Colour")
