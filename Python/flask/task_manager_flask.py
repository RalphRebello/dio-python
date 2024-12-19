from http.client import responses

from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tasks = [
    {
        'id':0,
        'responsavel':'rafael',
        'tarefa':'Desenvolver metodo GET',
        'status':'concluido'
    },
    {
        'id':1,
        'responsavel':'ralph',
        'tarefa':'Desenvolver metodo POST',
        'status':'pendente'}

]

@app.route('/tasks/', methods=['GET', 'PUT'])
def list_tasks():
    if request.method == 'GET':
        return jsonify(tasks)
    elif request.method == 'PUT':
        new_task = json.loads(request.data)
        id = len(tasks)
        new_task.update({'id': id})
        tasks.append(new_task)
        return jsonify(tasks)

@app.route('/tasks/<int:id>/', methods=['GET', 'POST', 'DELETE'])
def manage_tasks(id):
    if request.method == 'GET':
        return jsonify(tasks[id])
    if request.method == 'POST':
        tasks[id].update(json.loads(request.data))
        return jsonify(tasks[id])
    elif request.method == 'DELETE':
        tasks.pop(id)
        response = {'status': 'Success delete'}
        return response

if __name__ == '__main__':
    app.run(debug=True)
