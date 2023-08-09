import random
import string
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)
generated_codes = set()

def load_cities():
    cities_data = pd.read_csv("cities.csv")
    cities = cities_data["City"].tolist()
    return cities

def generate_code():
    while True:
        code = 'R' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if code not in generated_codes:
            generated_codes.add(code)
            return code

@app.route('/')
def index():
    cities = load_cities()
    return render_template('index.html', cities=cities)

@app.route('/generate_code')
def generate_unique_code():
    code = generate_code()
    return code

if __name__ == '__main__':
    app.run(debug=True)
