from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://www.fruityvice.com/api/fruit/all")
    fruit_list = response.json()

    fruits = []

    for fruit in fruit_list:
        fruits.append({
            'name': fruit["name"].capitalize(),
            'id': fruit["id"]
        })

    return render_template("index.html", fruits=fruits)

@app.route("/pokemon/<int:id>")
def fruity_detail():
    response = requests.get(f"https://www.fruityvice.com/api/fruit/{fruit["id"]}")
    data = response.json()

    family = data.get('family')
    order = data.get('order')
    genus = data.get('genus')
    


