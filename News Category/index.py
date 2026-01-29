import streamlit as st 
import joblib

model=joblib.load('model.joblib')

st.title('News Category Prediction')
st.markdown('Enter news below')
input_text=st.text_area(
    label='Enter news text that you want to predict',
    max_chars=1000, height=300)

if st.button("Predict Category"):
    prediction=model.predict([input_text])[0]
    st.success(f'Predicted Category is {prediction}')
