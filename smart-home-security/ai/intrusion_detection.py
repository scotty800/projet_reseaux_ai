import pandas as pd

data = pd.read_csv("data/sensor_data.csv")

alerts = data[((data["door"] == "OPEN") & (data["motion"] == "MOTION")) |
              ((data["window"] == "OPEN") & (data["motion"] == "MOTION"))]

alerts.to_csv("data/alerts.csv", index=False)
print("Alertes détectées :")
print(alerts)