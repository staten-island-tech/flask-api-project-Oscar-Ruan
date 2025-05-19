test = {"name": "Banana",
  "id": 1,
  "family": "Musaceae",
  "order": "Zingiberales",
  "genus": "Musa",
  "nutritions": {
    "calories": 96,
    "fat": 0.2,
    "sugar": 17.2,
    "carbohydrates": 22,
    "protein": 1
  }
}

for key, values in test['nutritions'].items():
    print(key, values)