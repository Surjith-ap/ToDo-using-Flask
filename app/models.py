from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    """
    User Model - stores user authentication data
    UserMixin provides Flask-Login methods: is_authenticated, is_active, etc.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    
    # Relationship: One user has many tasks
    tasks = db.relationship('Task', backref='owner', lazy=True, cascade='all, delete-orphan')

    def set_password(self, password):
        """Hash the password before storing"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verify the password against stored hash"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class Task(db.Model):
    """
    Task Model - stores user's tasks
    Each task belongs to one user
    """
    id = db.Column(db.Integer, primary_key=True)  # id column 
    title = db.Column(db.String(100), nullable=False)  # titles column
    status = db.Column(db.String(20), default="To-Do")  # status column (changed from "pending" to "To-Do")
    
    # Foreign key: Links this task to a user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Task {self.title}>'