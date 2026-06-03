import os
import pandas as pd
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample_data.csv")

df = pd.read_csv(csv_path)
print(df)

average_salary = df["salary"].mean()

print("\n Average Salary:",average_salary)


# bar chart 
plt.bar(df["Name"],df["salary"])

plt.title("Salary of Employees:")
plt.xlabel("Name")
plt.ylabel("salary")
plt.savefig ("bar_chart.png")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Age"],df["salary"])

plt.title("Age Vs Salary")

plt.xlabel("Age")
plt.ylabel("salary")
# print(df["Age"])
# print(df["salary"])
plt.savefig("Scatte_ralation.png")

plt.show()

import numpy as np
correlation = df[["Age","salary"]].corr()

plt.figure(figsize=(5,4))
plt.imshow(correlation.values, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(correlation.columns)), list(correlation.columns))
plt.yticks(range(len(correlation.columns)), list(correlation.columns))

plt.title("Correlation HeatMap")
plt.savefig("Correlation_Heatmap.png")

plt.show()


