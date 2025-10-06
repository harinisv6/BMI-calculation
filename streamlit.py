import streamlit as st
import requests

st.title("BMI Calculator")

# User inputs
weight = st.number_input("Enter your weight (kg)", min_value=1)
height = st.number_input("Enter your height (cm)", min_value=1)

if st.button("Calculate BMI"):
    # API URL
    url = "http://127.0.0.1:8000/bmi"

    # Make POST request with query parameters
    response = requests.post(url, params={"weight": weight, "height": height})

    if response.status_code == 200:
        data = response.json()
        st.success(f"BMI: {data['BMI']}")
        st.info(f"Category: {data['Category']}")
    else:
        st.error("Error connecting to API")
