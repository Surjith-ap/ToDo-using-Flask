"""
Vercel Serverless Entry Point
"""

from app import create_app

# Create the Flask application
app = create_app()

# Optional: add a test route (for debugging)
@app.route("/vercel-check")
def vercel_check():
    return "✅ Flask app running successfully on Vercel!"

# Vercel looks for `app` directly, so no need for handler or main block
# """
# Vercel Serverless Entry Point
# This file is required for Vercel deployment
# """

# from app import create_app
# import os

# # Create the Flask application
# app = create_app()

# # Vercel expects this for Python serverless functions
# def handler(environ, start_response):
#     """WSGI handler for Vercel"""
#     return app(environ, start_response)

# # For compatibility with different WSGI servers
# application = app

# # Debug info
# if __name__ == "__main__":
#     print("✅ Flask app created successfully")
#     print(f"Database: {app.config.get('SQLALCHEMY_DATABASE_URI', 'Not set')}")
