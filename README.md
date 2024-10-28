# Breast Cancer Prediction System

This project is a Breast Cancer Prediction System built using Streamlit for the frontend, Django for the backend, and a CSV dataset for calculating thresholds to classify tumors as malignant or benign based on user input. The app provides predictions by comparing input features to established thresholds without relying on heavy external dependencies like NumPy or TensorFlow.

## Features
- Prediction: Predicts if a tumor is malignant or benign based on input features.
- Threshold Calculation: Dynamically calculates thresholds for each feature from a dataset.
- Result Storage: Saves predictions and associated input data to a Django backend, accessible by admin users.
- User-Friendly Interface: Simple input form for users via Streamlit.

## Installation and Setup

### Requirements
1. Python 3.x
2. pip for installing dependencies.

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/breast-cancer-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd breast-cancer-prediction
   ```
3. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the Django server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
5. In a separate terminal, start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Project Structure
- app.py: Streamlit app for collecting user inputs and displaying predictions.
- predict.py: Prediction logic using custom threshold calculations.
- predictions: Django app managing prediction storage and retrieval.
- data.csv: Dataset file with tumor features used to calculate thresholds.

## Usage
1. Open the Streamlit app in a web browser.
2. Enter the relevant feature values.
3. Click the "Predict" button to receive a classification.
4. Predictions are saved to the Django backend for admin access.

## License
This project is open-source and available under the MIT License.
```

