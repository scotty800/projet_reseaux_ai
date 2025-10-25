import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("data/sensor_data.csv")
x = data[["temperature", "humidity", "light"]]

model = IsolationForest(contamination=0.1, random_state=42)
data["anomaly"] = model.fit_predict(x)

anomalies = data[data["anomaly"] == -1]
anomalies.to_csv("data/alerts.csv", index=False)

print("Anomalies détectées :")
print(anomalies)
