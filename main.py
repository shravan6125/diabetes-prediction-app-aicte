
import streamlit as st
import pickle
import numpy as np





# Title and subtitle
st.markdown('<h1 class="main-title">🩺 Diabetes Risk Predictor</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Enter your health metrics below to assess your diabetes risk using advanced machine learning</p>', unsafe_allow_html=True)

# User input form
with st.form("prediction_form"):
    st.markdown("### 📋 Health Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        pregnancies = st.number_input(
            "🤰 Pregnancies", 
            min_value=0, 
            max_value=20, 
            value=0,
            help="Number of times pregnant"
        )
        
        glucose = st.number_input(
            "🍯 Glucose Level", 
            min_value=0, 
            max_value=300, 
            value=100,
            help="Plasma glucose concentration (mg/dL)"
        )
        
        bp = st.number_input(
            "💓 Blood Pressure", 
            min_value=0, 
            max_value=200, 
            value=70,
            help="Diastolic blood pressure (mm Hg)"
        )
        
        skin = st.number_input(
            "📏 Skin Thickness", 
            min_value=0, 
            max_value=100, 
            value=20,
            help="Triceps skin fold thickness (mm)"
        )
    
    with col2:
        insulin = st.number_input(
            "💉 Insulin Level", 
            min_value=0, 
            max_value=1000, 
            value=80,
            help="2-Hour serum insulin (mu U/ml)"
        )
        
        bmi = st.number_input(
            "⚖️ BMI", 
            min_value=0.0, 
            max_value=70.0, 
            value=25.0,
            help="Body mass index (weight in kg/(height in m)^2)"
        )
        
        dpf = st.number_input(
            "🧬 Diabetes Pedigree Function", 
            min_value=0.0, 
            max_value=3.0, 
            value=0.5,
            help="Diabetes pedigree function (genetic predisposition)"
        )
        
        age = st.number_input(
            "🎂 Age", 
            min_value=1, 
            max_value=120, 
            value=30,
            help="Age in years"
        )
    
    submit = st.form_submit_button("🔍 Predict Diabetes Risk")

# Prediction
if submit:
    # Create input array
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    
    # Apply scaler if available
    if scaler:
        input_data = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    # Display results with enhanced styling
    st.markdown("### 📊 Prediction Result")
    
    if prediction == 1:
        st.error("🚨 **High Risk**: Based on the provided information, there is a high likelihood of diabetes. Please consult with a healthcare professional for proper diagnosis and treatment.")
    else:
        st.success("✅ **Low Risk**: Based on the provided information, there is a low likelihood of diabetes. Continue maintaining a healthy lifestyle!")
    
    # Add some additional info
    st.info("💡 **Note**: This prediction is based on machine learning analysis and should not replace professional medical advice. Always consult with healthcare providers for accurate diagnosis.")

# Footer
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    <p>Made with ❤️ by <strong>Shravan</strong> | Powered by Machine Learning</p>
</div>
""", unsafe_allow_html=True)
























