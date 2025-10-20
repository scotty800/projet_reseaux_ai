import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("security_analysis/risk_report.csv")
df["nb_ports"] = [len(str(p).split(",")) for p in df["Port"]]

x = df[["nb_ports"]]
model = IsolationForest(contamination=0.2, random_state=42)
df["anomaly"] = model.fit_predict(x)

print(df[df["anomaly"] == -1])