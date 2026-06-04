import pandas as pd
from pathlib import Path

script_dir = Path(__file__).resolve().parent
csv_path = script_dir / "data" / "train.csv"

if not csv_path.exists():
    raise FileNotFoundError(f"CSV file not found: {csv_path}")

df = pd.read_csv(csv_path)

features = [
    "GrLivArea",
    "BedroomAbvGr",
    "FullBath",
    "GarageCars",
    "TotalBsmtSF"
]

target = "SalePrice"
data = df[features + [target]]

print(data.head())
print("\nShape:",df.shape)

print("\nMissing Values:")
print(data.isnull().sum())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = data[features]
y = data[target]

X_train, X_test, y_train,y_test = train_test_split(
  x,
  y,
  test_size=0.2,
  random_state=42
)

model = LinearRegression()
model.fit(X_train,y_train)

predictions = model.predict(X_test)

print("First 5 Prediction:",predictions[:5])

print("\nActual Prices:",y_test.head())

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import numpy as np

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("\nR2 Score:", r2)  # Very good 
print("MAE:", mae)
print("RMSE:", rmse)


# graph Visualization

import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

plt.scatter(y_test,predictions)
plt.xlabel("Acutal Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()

# Residual Error Graph
errors = y_test - predictions
plt.figure(figsize=(8,6))
plt.scatter(predictions,errors)
plt.xlabel("Predicted Price")
plt.ylabel("Error")

plt.title("Residual Error Plot")

plt.axhline(y=0)

plt.show()

# Save to model Prediction
import pickle

model_dir = script_dir / "models"
model_dir.mkdir(parents=True, exist_ok=True)
model_path = model_dir / "house_price_model.pkl"

with open(model_path, "wb") as file:
    pickle.dump(model, file)

print(f"Model Saved Successfully at: {model_path}")


