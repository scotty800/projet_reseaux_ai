import pandas as pd
import os

os.makedirs("security_analysis", exist_ok=True)

data = pd.read_csv("data/reports/port_report.csv")
critical_ports = [22, 23, 445]

risks = data[data["PORT"].isin(critical_ports)]
risks["RISK"] = "HIGH"

risks.to_csv("security_analysis/risk_report.csv", index=False)