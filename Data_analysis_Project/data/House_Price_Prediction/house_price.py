import pandas as pd
df = pd.read_csv("Data_analysis_Project/data/House_Price_Prediction/data/train.csv")

# print(df.head())

# print("\nShape:",df.shape)

# print("\nColumns:")
# print(df.columns)

print("\nInfo:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum().sort_values(ascending=False).head(20))

# print("\nSalePrice Statistics:")
# print(df["SalePrice"].describe())