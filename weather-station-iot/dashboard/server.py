from flask import Flask, render_template_string
import csv

app = Flask(__name__)

HTML = """
<h1>📡 Station météo IoT</h1>
<table border=1 cellpadding=5>
<tr><th>Time</th><th>Temp</th><th>Hum</th><th>Press</th><th>Light</th><th>Events</th></tr>
{% for row in data %}
<tr>
<td>{{row[0]}}</td>
<td>{{row[1]}}°C</td>
<td>{{row[2]}}%</td>
<td>{{row[3]}} hPa</td>
<td>{{row[4]}}</td>
<td>{{row[5]}}</td>
</tr>
{% endfor %}
</table>

<meta http-equiv="refresh" content="5">
"""

@app.route("/")
def index():
    with open("../data/logs.csv") as f:
        data = list(csv.reader(f))[1:]  # skip header
    return render_template_string(HTML, data=data[-20:])

app.run(host="0.0.0.0", port=5000)
