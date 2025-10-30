import pandas as pd
from sklearn.ensemble import LabelEncoder
from sklearn.ensemble import IsolationForest

data = pd.read_csv("data/sensor_data.csv")

le = LabelEncoder()

data["door_enc"] = le.fit_transform(data["door"])
data["window_enc"] = le.fit_transform(data["window"])
data["motion_enc"] = le.fit_transform(data["motion"])

x = data[["door_enc", "window_enc", "motion_enc"]]
model = IsolationForest(contamination=0.1, random_state=42)
data["anomaly"] = model.fit_predict(x)

anomalies = data[data["anomaly"] == -1]
anomalies.to_csv("data/alerts.csv", index=False)
print(anomalies)