import streamlit as st
import requests
from predict import load_data, calculate_thresholds, predict_cancer

# Load data and calculate thresholds
data = load_data('data.csv')
thresholds = calculate_thresholds(data)

def main():
    st.title("Breast Cancer Prediction System")

    # Collect user input for each feature
    user_data = {}
    features = thresholds.keys()
    for feature in features:
        user_data[feature] = st.number_input(f"Enter {feature.replace('_', ' ').title()}", min_value=0.0, max_value=100.0, step=0.1)

    # Predict and submit results
    if st.button("Predict"):
        prediction = predict_cancer(user_data, thresholds)
        result = 'Malignant' if prediction == 'M' else 'Benign'
        st.write(f"The prediction is: {result}")

        # Prepare data for Django backend
        user_data['prediction_result'] = result

        response = requests.post("http://localhost:8000/predictions/save_prediction/", json=user_data)
        if response.status_code == 200:
            st.success("Prediction saved successfully!")
        else:
            st.error("Failed to save prediction.")

if __name__ == "__main__":
    main()
