import pandas as pd
from sklearn.ensemble import IsolationForest

try:
    data = pd.read_csv("data/temps.csv")

    # Vérifie qu'il y a bien des valeurs
    if data.empty or "temp" not in data.columns:
        raise ValueError("Fichier CSV vide ou colonne 'temp' manquante.")

    model = IsolationForest(contamination=0.05, random_state=42)
    model.fit(data[['temp']])

    data["alert"] = model.predict(data[['temp']])

    anomalies = data[data["alert"] == -1]
    print("Anomalies détectées :")
    print(anomalies)

except FileNotFoundError:
    print("Fichier data/temps.csv introuvable.")
except Exception as e:
    print("Erreur :", e)
