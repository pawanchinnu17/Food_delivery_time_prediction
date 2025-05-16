# 🚴‍♂️ Food Delivery Time Prediction

This project predicts food delivery time using an LSTM (Long Short-Term Memory) neural network. It leverages key features like delivery distance, delivery partner's age, and customer ratings to make accurate predictions. The final model is deployed with a **Streamlit** web interface and can be scaled in a production environment using **Docker**, **CI/CD pipelines**, and **AWS** cloud hosting.

---

## 📊 Features

- 📦 Predicts food delivery time based on:
  - Delivery partner's **age**
  - Delivery partner's **ratings**
  - **Distance** between restaurant and delivery location
- 🧠 Uses an **LSTM neural network** for time prediction
- 📈 Includes **visualizations** for exploratory data analysis
- 🌐 Real-time predictions via a **Streamlit** web app
- ☁️ Deployment-ready with **Docker**, **CI/CD**, and **AWS**

---

## 🧪 Tech Stack

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **Scikit-learn** for preprocessing
- **TensorFlow / Keras** for LSTM model
- **Streamlit** for web interface
- **Docker** for containerization
- **AWS** for deployment
- **GitHub** + **Git** for version control and CI/CD

---

## 🗃️ Dataset

The dataset contains the following features:

| Feature | Description |
|---------|-------------|
| `Delivery_person_Age` | Age of the delivery person |
| `Delivery_person_Ratings` | Customer rating of the delivery partner |
| `Restaurant_latitude`, `Restaurant_longitude` | Restaurant location |
| `Delivery_location_latitude`, `Delivery_location_longitude` | Customer location |
| `Time_taken(min)` | Target variable: delivery time |
| `Type_of_order`, `Type_of_vehicle` | Not used in this model, but present |

---

## 📊 Visualizations

The notebook includes:

- 📌 Pairplot of all numerical features
- 🔥 Correlation heatmap
- 📉 Delivery time distribution plot

These help you understand how each feature affects delivery time.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/food_delivery_time_prediction.git
cd food-delivery-time-prediction
