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
    
    fruits.sort(key=lambda f: f['id'])

    return render_template("index.html", fruits=fruits)


@app.route("/fruit/<int:id>")
def fruity_detail(id):
    response = requests.get(f"https://www.fruityvice.com/api/fruit/{id}")
    data = response.json()

    fruit_names = []
    fruit_value = []

    family = data.get('family')
    order = data.get('order')
    genus = data.get('genus')
    name = data.get('name').capitalize()

    for key, values in data['nutritions'].items():
        fruit_names.append(key)
        fruit_value.append(values)

    return render_template("fruits.html", fruit={
        'name': name,
        'id': id,
        'family': family,
        'order': order,
        'genus': genus,
        'fruit_names': fruit_names,
        'fruit_value': fruit_value
    })

if __name__ == '__main__':
    app.run(debug=True)