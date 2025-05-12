from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://www.fruityvice.com/api/fruit/all")
    data = response.json()
    fruits_list = data['results']