# streamlit_app.py

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("C:/Users/HP/premium_predictor.pkl")  # Make sure this file exists in your folder

st.title("💰 SmartPremium: Insurance Premium Predictor")

# User inputs
age = st.number_input("Age", 18, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
income = st.number_input("Annual Income (₹)", 50000, 5000000)
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
dependents = st.number_input("Number of Dependents", 0, 10)
education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
occupation = st.selectbox("Occupation", ["Employed", "Self-Employed", "Unemployed"])
health_score = st.slider("Health Score", 0, 100)
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
policy_type = st.selectbox("Policy Type", ["Basic", "Comprehensive", "Premium"])
claims = st.number_input("Previous Claims", 0, 20)
vehicle_age = st.number_input("Vehicle Age", 0, 30)
credit_score = st.number_input("Credit Score", 300, 900)
duration = st.number_input("Insurance Duration (years)", 1, 20)
smoking = st.selectbox("Smoking Status", ["Yes", "No"])
exercise = st.selectbox("Exercise Frequency", ["Daily", "Weekly", "Monthly", "Rarely"])
property_type = st.selectbox("Property Type", ["House", "Apartment", "Condo"])

# Predict button
if st.button("Predict Premium"):
    # Create DataFrame for prediction
    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Annual Income": income,
        "Marital Status": marital_status,
        "Number of Dependents": dependents,
        "Education Level": education,
        "Occupation": occupation,
        "Health Score": health_score,
        "Location": location,
        "Policy Type": policy_type,
        "Previous Claims": claims,
        "Vehicle Age": vehicle_age,
        "Credit Score": credit_score,
        "Insurance Duration": duration,
        "Smoking Status": smoking,
        "Exercise Frequency": exercise,
        "Property Type": property_type
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Premium: ₹{prediction:,.2f}")
