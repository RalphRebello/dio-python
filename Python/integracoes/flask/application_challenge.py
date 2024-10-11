from doctest import debug

from flask import Flask, jsonify


d = [
  {
    "Number": 1,
    "Name": "Mahesh",
    "Age": 25,
    "City": "Bangalore",
    "Country": "India"
  },
  {
    "Number": 2,
    "Name": "Alex",
    "Age": 26,
    "City": "London",
    "Country": "UK"
  },
  {
    "Number": 3,
    "Name": "David",
    "Age": 27,
    "City": "San Francisco",
    "Country": "USA"
  },
  {
    "Number": 4,
    "Name": "John",
    "Age": 28,
    "City": "Toronto",
    "Country": "Canada"
  },
  {
    "Number": 5,
    "Name": "Chris",
    "Age": 29,
    "City": "Paris",
    "Country": "France"
  }
]

app = Flask(__name__)

@app.route('/index', methods=['GET'])
def index():
    return jsonify(d)


if __name__ == '__main__':
    print('Servidor acessivel em: http://127.0.0.1:5000/index')

    app.run(port=5000, debug=True)
