from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Task
from database import init_db
from insights import generate_insights
from datetime import datetime

app = Flask(__name__)
CORS(app)
init_db(app)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    task = Task(
        title=data['title'],
        description=data.get('description', ''),
        priority=data['priority'],
        due_date=datetime.strptime(data['due_date'], '%Y-%m-%d').date(),
        status=data['status']
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task added', 'id': task.id})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    status = request.args.get('status')
    priority = request.args.get('priority')
    query = Task.query
    if status:
        query = query.filter_by(status=status)
    if priority:
        query = query.filter_by(priority=priority)
    tasks = query.order_by(Task.due_date).all()
    return jsonify([{
        'id': t.id,
        'title': t.title,
        'description': t.description,
        'priority': t.priority,
        'due_date': t.due_date.isoformat(),
        'status': t.status
    } for t in tasks])

@app.route('/tasks/<int:id>', methods=['PATCH'])
def update_task(id):
    data = request.json
    task = Task.query.get_or_404(id)
    if 'status' in data:
        task.status = data['status']
    if 'priority' in data:
        task.priority = data['priority']
    db.session.commit()
    return jsonify({'message': 'Task updated'})

@app.route('/insights', methods=['GET'])
def get_insights():
    return jsonify(generate_insights())

if __name__ == '__main__':
    app.run(debug=True)
