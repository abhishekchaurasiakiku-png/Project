import streamlit as st
import pandas as pd
import pickle

# Load Model
with open("Data_analysis_Project/data/House_Price_Prediction/models/house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction")
st.markdown("""
Predicts house prices using a Machine Learning Linear Regression model.
""")

st.write("Enter house details below")

# Inputs
GrLivArea = st.number_input("Living Area", min_value=0)

BedroomAbvGr = st.number_input("Bedrooms", min_value=0)

FullBath = st.number_input("Bathrooms", min_value=0)

GarageCars = st.number_input("Garage Capacity", min_value=0)

TotalBsmtSF = st.number_input("Basement Area", min_value=0)

# Prediction Button
if st.button("Predict Price"):

    new_house = pd.DataFrame({
        "GrLivArea": [GrLivArea],
        "BedroomAbvGr": [BedroomAbvGr],
        "FullBath": [FullBath],
        "GarageCars": [GarageCars],
        "TotalBsmtSF": [TotalBsmtSF]
    })

    prediction = model.predict(new_house)

    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")