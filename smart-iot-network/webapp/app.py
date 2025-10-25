from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    data = pd.read_csv("../data/sensor_data.csv")
    alerts = pd.read_csv("../data/alerts.csv")
    return render_template("index.html", tables=data.to_html(classes='table'), alerts=alerts.to_html(classes='table table-danger'))

if __name__ == "__main__":
    app.run(debug=True)
