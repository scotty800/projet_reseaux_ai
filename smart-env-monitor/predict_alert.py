import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("data/logs.csv")

model = IsolationForest(contamination=0.05).fit(data[["Temperature", "Humidity", "Light"]])
data["Anomaly"] = model.predict(data[["Temperature", "Humidity", "Light"]])

print(data[data["Anomaly"] == -1])