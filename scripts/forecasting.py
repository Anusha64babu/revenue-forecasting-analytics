import pandas as pd
from prophet import Prophet

# Load data
df = pd.read_csv("data/revenue_data.csv")

# Prophet format
df = df.rename(columns={"date": "ds", "revenue": "y"})

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=12, freq="MS")
forecast = model.predict(future)

forecast[["ds", "yhat"]].to_csv("data/forecast.csv", index=False)
print("Forecast generated")
