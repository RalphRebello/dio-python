from flask import Flask, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

devs = [
    {'nome':'Ralph',
     'habilidades':['python', 'flask']},
    {'nome':'Hina',
     'habilidades':['psicologia', 'logica']}
]

class EditDev(Resource):

    def get(self, id):
        try:
            dev = devs[id]
            return dev
        except IndexError:
            response = {'status': 'error', 'message': 'ID not found'}
            return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def delete(self, id):
        devs.pop(id)
        return {'status': 'success', 'message': 'Success removed'}

    def post(self, id):
        dados = json.loads(request.data)
        devs.append(dados)
        new_dev = len(devs)
        response = {'status': 'success', 'message': 'insert data with success'}
        response.update(devs[new_dev - 1])
        return response


api.add_resource(EditDev, '/dev/<int:id>/')


if __name__ == '__main__':
    app.run(debug=True)