from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Create db object globally
db = SQLAlchemy()

# Create login manager globally
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Configuration
    # Use environment variable for secret key
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Smart Database Configuration
    # Priority: DATABASE_URL env var > SQLite (for local dev)
    database_url = os.environ.get('DATABASE_URL')
    
    if database_url:
        # Production: Use PostgreSQL from environment variable
        # Fix for Heroku/some services that use postgres:// instead of postgresql://
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        print(f"✅ Using PostgreSQL database")
    else:
        # Local Development: Use SQLite
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
        print(f"✅ Using SQLite database (local development)")
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_pre_ping': True,  # Verify connections before using
        'pool_recycle': 300,    # Recycle connections after 5 minutes
    }

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    
    # Flask-Login configuration
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'info'

    # User loader callback
    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.tasks import task_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)

    # Create database tables automatically
    with app.app_context():
        try:
            db.create_all()
            print("✅ Database tables created successfully")
        except Exception as e:
            print(f"⚠️ Database initialization warning: {e}")

    return app