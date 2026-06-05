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
bar_colors = ["cyan", "magenta", "gold", "lime", "orange"]
plt.barh(df["Name"], df["salary"], color=bar_colors)

plt.title("Salary of Employees:")
plt.xlabel("Name")
plt.ylabel("salary")
plt.savefig("bar_chart.png")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["Age"], df["salary"], color="cyan", s=80)
plt.plot(df["Age"], df["salary"], color="cyan", linestyle="-.", linewidth=1)

plt.title("Age Vs Salary")

plt.xlabel("Age")
plt.ylabel("salary")
# print(df["Age"])
# print(df["salary"])
plt.savefig("Scatte_ralation.png")

plt.show()

# heatmap plot
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

# pie chart
plt.figure(figsize=(6,6))
explode = [0.1, 0, 0, 0, 0]
plt.pie(df["salary"], labels=df["Name"], autopct="%.0f%%", startangle=90, explode=explode,shadow=True, colors=["cyan", "magenta", "gold", "lime", "orange"])
plt.title("Salary Distribution by Employee")
plt.savefig("pie_chart.png")
plt.show()




