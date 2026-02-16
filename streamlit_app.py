import streamlit as st
import requests

st.set_page_config(page_title="Heart Attack API Tester", layout="centered")
st.title("Heart Attack Prediction – Streamlit UI (Testing Railway API)")

# ✅ Use your Railway endpoint
API_URL = "https://web-production-0d637.up.railway.app/predict"

st.subheader("Enter patient values")

age = st.number_input("Age", min_value=1, max_value=120, value=45)

gender = st.selectbox("Gender (0/1)", [0, 1], index=1)

heart_rate = st.number_input("Heart rate", min_value=20.0, max_value=250.0, value=75.0, step=1.0)

sys_bp = st.number_input("Systolic blood pressure", min_value=50.0, max_value=300.0, value=120.0, step=1.0)

dia_bp = st.number_input("Diastolic blood pressure", min_value=20.0, max_value=200.0, value=80.0, step=1.0)

blood_sugar = st.number_input("Blood sugar", min_value=0.0, max_value=1000.0, value=120.0, step=1.0)

ck_mb = st.number_input("CK-MB", min_value=0.0, max_value=500.0, value=2.0, step=0.01)

troponin = st.number_input("Troponin", min_value=0.0, max_value=50.0, value=0.010, step=0.001, format="%.3f")


# ✅ IMPORTANT:
# This payload matches the JSON keys I gave in the updated FastAPI code:
# Heart_rate, Systolic_blood_pressure, etc.
payload = {
    "Age": float(age),
    "Gender": int(gender),
    "Heart_rate": float(heart_rate),
    "Systolic_blood_pressure": float(sys_bp),
    "Diastolic_blood_pressure": float(dia_bp),
    "Blood_sugar": float(blood_sugar),
    "CK_MB": float(ck_mb),
    "Troponin": float(troponin)
}

if st.button("Predict"):
    with st.spinner("Calling Railway API..."):
        try:
            res = requests.post(API_URL, json=payload, timeout=30)
            st.write("Status:", res.status_code)

            # show response
            try:
                data = res.json()
                st.success("Response received ✅")
                st.json(data)
            except Exception:
                st.warning("Non-JSON response:")
                st.text(res.text)

        except Exception as e:
            st.error(f"Request failed: {e}")
