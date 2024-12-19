from flask import Flask, request, jsonify
import json


app = Flask(__name__)

devs = [
    {'nome':'Ralph',
     'habilidades':['python', 'flask']},
    {'nome':'Hina',
     'habilidades':['psicologia', 'logica']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def edit_dev(id):
    if request.method == 'GET':
        try:
            dev = devs[id]
            print(dev)
            return jsonify(dev)
        except IndexError:
            response = {'status':'error', 'message':'ID not found'}
            return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status':'success', 'message':'Success removed'})


@app.route('/dev/', methods=['POST', 'GET'])
def add_dev():
    if request.method == 'POST':
        dados = json.loads(request.data)
        devs.append(dados)
        new_dev = len(devs)
        response = {'status': 'success', 'message': 'insert data with success'}
        response.update(devs[new_dev-1])
        print(response)
        return jsonify(response)
    elif request.method == 'GET':
        return jsonify(devs)


if __name__ == '__main__':
    app.run(debug=True)