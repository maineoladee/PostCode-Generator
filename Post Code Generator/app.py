import random
import string
import pandas as pd
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
generated_postcodes = {}

def load_streets():
    streets_data = pd.read_csv("streets_lagos.csv")
    streets = streets_data["Street"].tolist()
    return streets

def load_postcodes():
    try:
        with open("postcodes.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def generate_postcode(street):
    if street in generated_postcodes:
        return generated_postcodes[street]

    letters = random.choices(string.ascii_uppercase, k=5)
    digit = random.choice(string.digits)
    postcode = ''.join(letters) + digit

    generated_postcodes[street] = postcode
    save_postcodes()
    return postcode

def save_postcodes():
    with open("postcodes.json", "w") as file:
        json.dump(generated_postcodes, file)

@app.route('/')
def index():
    return render_template('index.html', streets=load_streets())

@app.route('/generate_postcode', methods=['POST'])
def generate_unique_postcode():
    street = request.form.get('street')
    postcode = generate_postcode(street)
    return jsonify(postcode)

if __name__ == '__main__':
    generated_postcodes = load_postcodes()
    app.run(debug=True)
