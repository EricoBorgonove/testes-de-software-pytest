from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de dados fictícia
tasks = [
    {"id": 1, "task": "Estudar Flask"},
    {"id": 2, "task": "Construir uma API"},
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    new_task = request.get_json()
    tasks.append({"id": len(tasks) + 1, "task": new_task["task"]})
    return jsonify({"message": "Tarefa criada com sucesso!"}), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Tarefa removida com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)
