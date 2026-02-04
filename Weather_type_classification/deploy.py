import streamlit as st
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "knn_model.joblib")
model = joblib.load(MODEL_PATH)

st.title("Weather Prediction")

temperature=st.number_input(label="Temperature", min_value=0.0,max_value=50.0)
humidity=st.number_input(label="Humidity", min_value=0.0,max_value=100.0)
Windspeed=st.number_input(label="WindSpeed", min_value=0.0,max_value=50.0)
Pressure=st.number_input(label="Pressure", min_value=980.0,max_value=1050.0)

sample=[[temperature,humidity,Windspeed,Pressure]]

if st.button("Predict"):
    prediction=model.predict(sample)[0]
    st.success(f"🌻Predicted Weather is {prediction}🌻 ")
else:
        # Display warning if out of valid range
        st.warning("⚠️ Enter a valid range for prediction.")