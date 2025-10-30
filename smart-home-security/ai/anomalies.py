import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest

# Lecture des données
data = pd.read_csv("data/sensor_data.csv")

# Encodage séparé pour chaque capteur
door_le = LabelEncoder()
data["door_enc"] = door_le.fit_transform(data["door"])

window_le = LabelEncoder()
data["window_enc"] = window_le.fit_transform(data["window"])

motion_le = LabelEncoder()
data["motion_enc"] = motion_le.fit_transform(data["motion"])

# Sélection des colonnes numériques
x = data[["door_enc", "window_enc", "motion_enc"]]

# Modèle de détection d'anomalies
model = IsolationForest(contamination=0.1, random_state=42)
data["anomaly"] = model.fit_predict(x)

# Extraction et sauvegarde des anomalies
anomalies = data[data["anomaly"] == -1]
anomalies.to_csv("data/alerts.csv", index=False)

# Affichage
print("Anomalies détectées :")
print(anomalies)
