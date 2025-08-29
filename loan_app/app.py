import streamlit as st
import numpy as np
import pickle

# Load trained model
with open('loan_model_pickle.sav', 'rb') as file:
    model = pickle.load(file)

# Streamlit App
st.title("🏦 Loan Approval Prediction App")
st.write("Enter the applicant's information to predict if their loan will be approved.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", [0, 1, 2, 4])  # 4 represents '3+'
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Convert inputs to model format
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
property_area = {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]

# Prediction
if st.button("Predict Loan Approval"):
    input_data = np.array([gender, married, dependents, education, self_employed,
                           applicant_income, coapplicant_income, loan_amount,
                           loan_term, credit_history, property_area]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")
