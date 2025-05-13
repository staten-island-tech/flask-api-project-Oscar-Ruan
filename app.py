from flask import Flask, render_template
import requests

app = Flask(__name__)
id = 3

def pokemon_detail(id):
    response = requests.get(f"https://www.fruityvice.com/api/fruit/{id}")
    fruit_details = response.json()
    for fruit in fruit_details:
        print(fruit)

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
def pokemon_detail(id):
    response = requests.get(f"https://www.fruityvice.com/api/fruit/{id}")
    fruit_details = response.json()
    for fruit in fruit_details:
        print(fruit)