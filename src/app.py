import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/student_model.pkl")

# Title
st.title("🎓 Student Performance Predictor")

st.write("Enter student details")

# Inputs
study_hours = st.number_input(
    "Study Hours",
    min_value=0,
    max_value=15,
    value=5
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=80
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0,
    max_value=100,
    value=70
)

assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=7
)

sleep_hours = st.number_input(
    "Sleep Hours",
    min_value=0,
    max_value=12,
    value=7
)

# Prediction
if st.button("Predict Final Score"):

    student_data = np.array([[
        study_hours,
        attendance,
        previous_score,
        assignments,
        sleep_hours
    ]])

    prediction = model.predict(student_data)

    st.success(
        f"Predicted Final Score: {prediction[0]:.2f}"
    )