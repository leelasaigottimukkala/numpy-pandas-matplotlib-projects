import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun"],
    "Electronics": [12000,15000,17000,16000,18000,20000],
    "Clothing": [8000,9000,8500,9500,10000,11000],
    "Groceries": [6000,6500,7000,7200,7500,8000]
}

df = pd.DataFrame(data)
df["Total_Revenue"] = df[["Electronics","Clothing","Groceries"]].sum(axis=1)

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.plot(df["Month"], df["Total_Revenue"], marker="o")
plt.title("Total Revenue Trend")

plt.subplot(2,2,2)
plt.plot(df["Month"], df["Electronics"], label="Electronics")
plt.plot(df["Month"], df["Clothing"], label="Clothing")
plt.plot(df["Month"], df["Groceries"], label="Groceries")
plt.legend()
plt.title("Category-wise Revenue")

plt.subplot(2,2,3)
plt.bar(df["Month"], df["Total_Revenue"])
plt.title("Monthly Revenue Comparison")

plt.tight_layout()
plt.show()
