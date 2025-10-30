from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.String(10), nullable=False)  # Low, Medium, High
    due_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # Open, InProgress, Done
