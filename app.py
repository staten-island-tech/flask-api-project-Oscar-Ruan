from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get("https://www.fruityvice.com/api/fruit/all")
    data = response.json()
    fruit_list = data

    fruits = []

    for fruit in fruit_list:
        fruits.append({
            'name': fruit['name'].capitalize(),
            'id': fruit['id']
        })

    return render_template("index.html", fruit=fruit)

@app.route("/pokemon/<int:id>")
def fruity_detail(id):
    response = requests.get(f"https://www.fruityvice.com/api/fruit/{id}")
    data = response.json()
    for fruit in data:
        print(fruit)

if __name__ == '__main__':
    app.run(debug=True)