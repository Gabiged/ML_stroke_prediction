import streamlit as st
import joblib
import pandas as pd


model = joblib.load('essembled_model.joblib')


def predict_stroke(features):
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]
    return prediction, probability


def main():
    st.title('Stroke Prediction App')
    st.write("Enter the required information for stroke prediction:")

    # Create input fields for user to enter information
    gender = st.selectbox("Gender", ("Male", "Female"))
    age = st.number_input("Age", min_value=0.1, max_value=100.0)
    hypertension = st.selectbox("Hypertension", ("Yes", "No"))
    heart_disease = st.selectbox("Heart Disease", ("Yes", "No"))
    avg_glucose_level = st.number_input("Average Glucose Level", min_value=0.0)
    bmi = st.number_input("BMI", min_value=0.0)

    if st.button("Predict Stroke"):
        input_data = pd.DataFrame({
            "gender": [1 if gender == "Male" else 0],
            "age": [age],
            "hypertension": [1 if hypertension == "Yes" else 0],
            "heart_disease": [1 if heart_disease == "Yes" else 0],
            "avg_glucose_level": [avg_glucose_level],
            "bmi": [bmi],
        })

        prediction, probability = predict_stroke(input_data)

        if prediction[0] == 0:
            st.write("You have a low risk of stroke.")
        else:
            st.write("You are at a high risk of stroke.")
            st.write("Probability of stroke:", probability)


if __name__ == "__main__":
    main()
