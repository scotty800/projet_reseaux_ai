import pandas as pd

data = pd.read_csv("data/sensor_data.csv")
alerts = data[(data["temperature"] > 28) | 
              (data["humidity"] > 60) | 
              (data["light"] > 900)]

alerts.to_csv("data/alerts.csv", index=False)

print("Alertes détectées :")
print(alerts)