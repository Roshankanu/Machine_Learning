import streamlit as st 
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.joblib")
model = joblib.load(MODEL_PATH)

st.title('News Category Prediction')
st.markdown('Enter news below')
input_text=st.text_area(
    label='Enter news text that you want to predict',
    max_chars=1000, height=300)

if st.button("Predict Category"):
    if not input_text.strip():
        st.warning("Please enter text to search")
    else:
        prediction=model.predict([input_text])[0]
        st.success(f'Predicted Category is {prediction}')

