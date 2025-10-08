import pandas as pd

data = pd.read_csv("system_metrics.csv")

anomalies = data[data["cpu_percent"] > 90]

print("Anomalies detected :")
print(anomalies)