import pickle
import pandas as pd

# Load module
with open("Data_analysis_Project/data/House_Price_Prediction/models/house_price_model.pkl","rb") as file:
  model = pickle.load(file)
  
# user Input
GrLivArea = float(input("Enter Living Area: "))
BedroomAbvGr = int(input("Enter Number of Bedrooms: "))
FullBath = int(input("Enter Number of Bathrooms: "))
GarageCars = int(input("Enter Garage Capacity: "))
TotalBsmtSF = float(input("Enter Basement Area: "))

# creating data frame

new_house = pd.DataFrame({
    "GrLivArea": [GrLivArea],
    "BedroomAbvGr": [BedroomAbvGr],
    "FullBath": [FullBath],
    "GarageCars": [GarageCars],
    "TotalBsmtSF": [TotalBsmtSF]
})

# prediction
predict_price = model.predict(new_house)

print("\nPredicted House Price: $",round(predict_price[0],2))