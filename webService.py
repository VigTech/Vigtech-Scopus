#!flask/bin/python
from flask import Flask, jsonify
from administradorConsultas import AdministradorConsultas

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})
    
from flask import abort

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})
    
@app.route('/consultaScopus/v1.0/<consulta>', methods=['GET'])
def get_taski(consulta):
	ac = AdministradorConsultas()
	ac.descargar_papers(consulta)
	return jsonify({'titulos':ac.titulos_descargas})

if __name__ == '__main__':
    app.run(host='172.17.9.195', debug=True)
