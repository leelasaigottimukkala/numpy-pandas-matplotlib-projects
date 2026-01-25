import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107],
    "Math": [78, 85, 90, 60, 72, 88, 95],
    "Science": [82, 80, 88, 65, 70, 90, 92],
    "English": [75, 78, 85, 58, 68, 86, 90],
    "Attendance": [85, 90, 95, 70, 80, 92, 98]
}

df = pd.DataFrame(data)

df["Average_Marks"] = df[["Math", "Science", "English"]].mean(axis=1)

def performance(avg):
    if avg >= 85:
        return "Good"
    elif avg >= 70:
        return "Average"
    else:
        return "Poor"

df["Performance"] = df["Average_Marks"].apply(performance)

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.bar(["Math","Science","English"], df[["Math","Science","English"]].mean())
plt.title("Subject-wise Average Marks")

plt.subplot(2,2,2)
plt.scatter(df["Attendance"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.grid()

plt.subplot(2,2,3)
plt.hist(df["Average_Marks"], bins=5)
plt.title("Average Marks Distribution")

plt.subplot(2,2,4)
df["Performance"].value_counts().plot(kind="bar")
plt.title("Performance Categories")

plt.tight_layout()
plt.show()
