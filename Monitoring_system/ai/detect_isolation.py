import pandas as pd
from sklearn.ensemble import IsolationForest

data = pd.read_csv("system_metrics.csv")

x = data[["cpu_percent", "ram_percent"]]

clf = IsolationForest(contamination=0.1, random_state=42)
data["anomaly"] = clf.fit_predict(x)

print(data[data["anomaly"] == -1])
