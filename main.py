import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    saved = pickle.load(f)

model = saved["model"]
scaler = saved.get("scaler")  # Optional
columns = saved.get("columns")  # Optional

st.set_page_config(page_title="Diabetes Predictor", layout="centered")

# Title
st.title(" Diabetes Prediction App")
st.write("Enter the details below to predict diabetes risk.")

# User input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input("Pregnancies", 0, 20)
        glucose = st.number_input("Glucose", 0, 300)
        bp = st.number_input("Blood Pressure", 0, 200)
        skin = st.number_input("Skin Thickness", 0, 100)
    with col2:
        insulin = st.number_input("Insulin", 0, 1000)
        bmi = st.number_input("BMI", 0.0, 70.0)
        dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
        age = st.number_input("Age", 1, 120)

    submit = st.form_submit_button("Predict")

# Prediction
if submit:
    input_data = np.array([[pregnancies, glucose, bp, skin,
                            insulin, bmi, dpf, age]])

    # Apply scaler if available
    if scaler:
        input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error(" High Risk: The person is likely to have diabetes.")
    else:
        st.success(" Low Risk: The person is unlikely to have diabetes.")

# Footer
st.markdown("---")
st.markdown("Made with by Shravan")
