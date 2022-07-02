from flask import Flask, jsonify, request

app = Flask(__name__)
cars = [
    {
        'name': 'Ciaz',
        'spec': [
            {
                'variant': 'Sedan',
                'price': '12L',
                'company': 'Maruthi'
            }
        ]
    },
    {
        'name': 'Harrier',
        'spec': [
            {
                'variant': 'SUV',
                'price': '25L',
                'company': 'Tata'
            }
        ]
    }
]


@app.route('/')
def home():
    return "Hello World"


@app.route('/car', methods=['POST'])
def create_car():
    request_data = request.get_json()
    new_car = {
        'name': request_data['name'],
        'spec': []
    }
    cars.append(new_car)
    return jsonify(new_car)


@app.route('/car/<string:name>')
def get_car_name(name):
    for car in cars:
        if(car['name'] == name):
            return jsonify(car)
    return jsonify({'message': 'car not found'})


@app.route('/car')
def get_all_car_name():
    return jsonify({'cars': cars})


@app.route('/car/<string:name>/spec', methods=['POST'])
def create_car_spec(name):
    request_data = request.get_json()
    for car in cars:
        if(car['name'] == name):
            new_spec = {
                'name': request_data['name'],
                'price': request_data['price'],
                'company': request_data['company']
            }
            car['specs'].append(new_spec)
            return jsonify(new_spec)
    return jsonify({'message':'car not found'})


@app.route('/car/<string:name>/spec')
def get_car_spec(name):
    for car in cars:
        if(car['name'] == name):
            return jsonify(car['specs'])
    return jsonify({'message': 'car not found'})


app.run(port=7600)