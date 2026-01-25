import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Day": [1,2,3,4,5,6,7],
    "Open": [100,102,101,103,105,104,106],
    "Close": [102,101,103,105,104,106,108],
    "Volume": [2000,2200,2100,2300,2500,2400,2600]
}

df = pd.DataFrame(data)
df["Daily_Change"] = df["Close"] - df["Open"]

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.plot(df["Day"], df["Open"], label="Open")
plt.plot(df["Day"], df["Close"], label="Close")
plt.legend()
plt.title("Price Trend")

plt.subplot(2,2,2)
plt.bar(df["Day"], df["Volume"])
plt.title("Trading Volume")

plt.subplot(2,2,3)
plt.scatter(df["Open"], df["Close"])
plt.title("Open vs Close Price")
plt.xlabel("Open")
plt.ylabel("Close")

plt.tight_layout()
plt.show()
