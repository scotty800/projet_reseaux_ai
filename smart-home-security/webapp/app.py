import os
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data_file = "../data/sensor_data.csv"

    if not os.path.exists(data_file):
        return render_template("index.html", error="Aucune donnée disponible — fichier introuvable.", data=[], columns=[])

    try:
        data = pd.read_csv(data_file)
        if data.empty:
            return render_template("index.html", error="Aucune donnée enregistrée pour l'instant.", data=[], columns=[])
    except pd.errors.EmptyDataError:
        return render_template("index.html", error="Fichier vide — en attente de nouvelles données.", data=[], columns=[])

    # Convertit le DataFrame en liste de dictionnaires pour Jinja2
    records = data.to_dict(orient="records")
    columns = list(data.columns)

    return render_template("index.html", error=None, data=records, columns=columns)

if __name__ == "__main__":
    app.run(debug=True)
