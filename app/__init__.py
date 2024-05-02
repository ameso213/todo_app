from flask import Flask, request, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')

class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def update_task(self, task_id, new_task):
        if task_id < len(self.tasks):
            self.tasks[task_id] = new_task
            return {"message": "Task updated successfully."}
        else:
            return {"error": "Invalid task ID."}, 404

    def delete_task(self, task_id):
        if task_id < len(self.tasks):
            del self.tasks[task_id]
            return {"message": "Task deleted successfully."}
        else:
            return {"error": "Invalid task ID."}, 404

    def display_tasks(self):
        if self.tasks:
            return {"tasks": self.tasks}
        else:
            return {"message": "No tasks in the list."}


todo_list = TodoApp()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(todo_list.display_tasks())

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json.get('task')
    if task:
        todo_list.add_task(task)
        return {"message": "Task added successfully."}
    else:
        return {"error": "Task not provided."}, 400

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    new_task = request.json.get('task')
    if new_task:
        return jsonify(todo_list.update_task(task_id, new_task))
    else:
        return {"error": "New task not provided."}, 400

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    return jsonify(todo_list.delete_task(task_id))

if __name__ == "__main__":
    app.run(debug=True)
