from app import create_app, db
from app.models import Task

app = create_app()

# Initialize database tables
with app.app_context():
    db.create_all()

# For Vercel serverless deployment
# Vercel will use the 'app' variable

if __name__ == "__main__":
    app.run(debug=True)
