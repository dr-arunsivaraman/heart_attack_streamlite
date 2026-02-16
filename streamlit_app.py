import streamlit as st
import requests

st.title("Heart Attack Prediction – API Tester (Railway)")

API_URL = "https://web-production-0d637.up.railway.app/predict"

st.subheader("Enter values (same as dataset columns)")

age = st.number_input("Age", min_value=1, max_value=120, value=45)

gender = st.selectbox("Gender (0/1)", [0, 1], index=1)  # change labels if needed

heart_rate = st.number_input("Heart rate", min_value=20, max_value=250, value=75)

sys_bp = st.number_input("Systolic blood pressure", min_value=50, max_value=300, value=120)

dia_bp = st.number_input("Diastolic blood pressure", min_value=20, max_value=200, value=80)

blood_sugar = st.number_input("Blood sugar", min_value=0.0, max_value=1000.0, value=120.0, step=1.0)

ck_mb = st.number_input("CK-MB", min_value=0.0, max_value=500.0, value=2.0, step=0.01)

troponin = st.number_input("Troponin", min_value=0.0, max_value=50.0, value=0.01, step=0.001, format="%.3f")

# IMPORTANT: send ONLY input features (not Result)
payload = {
    "Age": age,
    "Gender": gender,
    "Heart rate": heart_rate,
    "Systolic blood pressure": sys_bp,
    "Diastolic blood pressure": dia_bp,
    "Blood sugar": blood_sugar,
    "CK-MB": ck_mb,
    "Troponin": troponin
}

if st.button("Predict"):
    with st.spinner("Calling API..."):
        try:
            r = requests.post(API_URL, json=payload, timeout=30)
            st.write("Status:", r.status_code)

            try:
                st.json(r.json())
            except Exception:
                st.text(r.text)

        except Exception as e:
            st.error(f"Request failed: {e}")
