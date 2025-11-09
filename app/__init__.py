from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#create db object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    #csrf protection key
    app.config['SECRET_KEY'] = 'your-secret-key'
    #the db you are using 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    #to track modifications
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #connecting the app with db
    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import task_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    return app
    