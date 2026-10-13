import streamlit as st
import pandas as pd
import mlflow.sklearn

st.set_page_config(page_title="FAANG Stock Predictor", layout="wide")
st.title("FAANG Stock Price Prediction App")


model_path = "runs:/f3995bba11ca4e7081b30b11ed53b6fa/ui_ready_rf_model"

try:
    model = mlflow.sklearn.load_model(model_path)
except Exception as e:
    st.error("Model not loading .Check Server/MLflow.")
    st.stop()

st.subheader("Enter Stock Details")


col1, col2, col3 = st.columns(3)

with col1:
    open_price = st.number_input("Open Price", value=150.0)
    high_price = st.number_input("High Price", value=155.0)

with col2:
    low_price = st.number_input("Low Price", value=149.0)
    volume = st.number_input("Volume", value=10000000)

with col3:
    ticker = st.selectbox("Company", ["AAPL", "GOOGL", "META", "AMZN", "NFLX"])
    predict_btn = st.button("Predict Close Price")

if predict_btn:
   
    input_data = pd.DataFrame({
        'Open': [open_price],
        'High': [high_price],
        'Low': [low_price],
        'Volume': [volume],
        'Ticker_AMZN': [1 if ticker == 'AMZN' else 0],
        'Ticker_GOOGL': [1 if ticker == 'GOOGL' else 0],
        'Ticker_META': [1 if ticker == 'META' else 0],
        'Ticker_NFLX': [1 if ticker == 'NFLX' else 0]
    })
    
   
    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Predicted Close Price: ${prediction:.2f}")
    except Exception as e:
        st.error(f"Prediction-la error: {e}")