import streamlit as st
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "knn_model.joblib")
model = joblib.load(MODEL_PATH)

st.title("Iris Flower Classifier 🌻")

model=joblib.load('knn_model.joblib')
sepal_length=st.number_input(label="Sepal Length", min_value=0.0,max_value=10.0)
sepal_width=st.number_input(label="Sepal Width", min_value=0.0,max_value=10.0)
petal_length=st.number_input(label="Petal Length", min_value=0.0,max_value=10.0)
petal_width=st.number_input(label="Petal Width", min_value=0.0,max_value=10.0)

sample=[[sepal_length,sepal_width,petal_length,petal_width]]

if st.button("Predict"):
    prediction=model.predict(sample)[0]
    st.success(f"🌻Predicted Species is {prediction}🌻 ")