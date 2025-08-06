import flask
from Manager import Manager

manager = Manager()

app = flask.Flask(__name__)

@app.route('/tasks', methods=['POST'])
def create():
    values = flask.request.get_json()
    manager.createTask(values.get('author'), values.get('task'))
    response = {
        'mensagem':'task criada com sucesso!'
    }
    return flask.jsonify(response), 200

@app.route("/tasks", methods=['GET'])
def getTasks():
    tasks = manager.GetTasks()
    response = []
    for task in tasks:
        newItem = {
            "id": task.getID() ,
            "author": task.getAuthor(),
            "task": task.getTask()
        }
        response.append(newItem)
    return flask.jsonify(response) 

@app.route("/tasks", methods=['DELETE'])
def delTasks():
    values = flask.request.get_json()
    id_value = values.get('id')

    success = manager.deleteTask(id_value)
    if success:
        return flask.jsonify({"mensagem": "Task deletada com sucesso"}), 200
    else:
        return flask.jsonify({"erro": "Task não encontrada"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)