import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2019-01-01", end="2024-12-01", freq="MS")

revenue = []
base = 50000

for i, date in enumerate(dates):
    seasonal = 10000 * np.sin(2 * np.pi * i / 12)
    growth = i * 1200
    noise = np.random.normal(0, 5000)
    revenue.append(base + seasonal + growth + noise)

df = pd.DataFrame({
    "date": dates,
    "revenue": revenue
})

df.to_csv("data/revenue_data.csv", index=False)
print("Revenue dataset created")
