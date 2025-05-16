import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import math

# Load the trained model
model = tf.keras.models.load_model('lstm_delivery_model.h5')

# Set Streamlit page config
st.set_page_config(page_title="Food Delivery Time Predictor", layout="centered")

# App title
st.title("🛵 Food Delivery Time Prediction App")
st.markdown("""
Predict delivery time based on:
- Delivery partner's **age**
- **Ratings**
- **Distance** between restaurant and customer  
""")

# Sidebar Inputs
st.sidebar.header("Enter Delivery Details")

age = st.sidebar.slider("Delivery Partner Age", 18, 60, 30)
rating = st.sidebar.slider("Delivery Partner Rating", 1.0, 5.0, 4.5, step=0.1)
distance = st.sidebar.slider("Distance (in KM)", 0.1, 20.0, 2.0, step=0.1)

# MinMaxScaler should match training scaling
scaler = MinMaxScaler()
# Fake fit to create same scale shape as training
scaler.fit([[18, 1.0, 0.1], [60, 5.0, 20.0]])

# Transform input
input_data = np.array([[age, rating, distance]])
input_scaled = scaler.transform(input_data).reshape((1, 1, 3))

# Predict
if st.sidebar.button("Predict Delivery Time"):
    prediction = model.predict(input_scaled)
    predicted_time = prediction[0][0]
    st.success(f"⏱ Estimated Delivery Time: **{predicted_time:.2f} minutes**")
