from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    data = pd.read_csv("../data/temps.csv")
    return data.to_html()

if __name__ == "__main__":
    app.run(debug=True)
