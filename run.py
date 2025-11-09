from app import create_app, db
from app.models import Task
from dotenv import load_dotenv

# Load environment variables from .env file (for local development)
load_dotenv()

# Create the Flask application
app = create_app()

# Initialize database tables
with app.app_context():
    db.create_all()

# For Vercel serverless deployment
# Vercel will use the 'app' variable

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
