'''from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Task

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'title': task.title} for task in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Deleted'})
    return jsonify({'message': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)'''




from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import db, Task
import pandas as pd

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'title': task.title} for task in tasks]
    return jsonify(task_list)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Deleted'})

@app.route('/export/excel', methods=['GET'])
def export_excel():
    tasks = Task.query.all()
    if not tasks:
        return jsonify({'message': 'No tasks to export'}), 404
    task_list = [{'id': task.id, 'title': task.title} for task in tasks]
    df = pd.DataFrame(task_list)
    file_name = 'tasks.xlsx'
    df.to_excel(file_name, index=False)
    return send_file(file_name, as_attachment=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tables created and database.db should be visible now")
    app.run(debug=True)
