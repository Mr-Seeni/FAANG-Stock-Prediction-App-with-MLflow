*FAANG Stock Price Prediction 📈*

**Project Overview**

This project is an end-to-end Machine Learning web application that predicts the closing stock prices of FAANG companies (Facebook/Meta, Apple, Amazon, Netflix, Google). It utilizes historical stock market data, a Random Forest regression model, MLflow for experiment tracking, and Streamlit for the user interface.

**Tech Stack**

* Language: Python

* Machine Learning: Scikit-learn (Random Forest Regressor, Pipeline, StandardScaler)

* Experiment Tracking: MLflow

* Web Framework: Streamlit

* Data Manipulation: Pandas, NumPy

**Project Architecture**

* Data Preprocessing: Handled missing values, encoded categorical features (Ticker symbols), and applied feature scaling.

* Model Training: Trained a robust Random Forest model. Packaged the scaler and model into a single sklearn.pipeline to handle raw user inputs seamlessly.

* MLflow Integration: Tracked model metrics (MAE, RMSE, R2 Score) and saved the best-performing model as a serialized artifact (ui_ready_rf_model).

* Streamlit Deployment: Built an interactive UI that loads the model directly from the MLflow registry to make real-time predictions based on user inputs (Open, High, Low, Volume).

**How to Run Locally**

1. Clone the Repository

```bash
git clone 
cd 
```

2. Install Dependencies

Ensure you have Python installed, then create a virtual environment and install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit App

Launch the web application using the following command:
```bash
streamlit run app.py
```
The app will open automatically in your default web browser (usually at http://localhost:8501).