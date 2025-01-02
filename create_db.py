# create_db.py
from application import app, db  # Import your app and db instance from your app folder

# Set up the application context and create tables
with app.app_context():
    db.create_all()
    print("Database tables created!")
