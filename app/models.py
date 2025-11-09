from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True) #id column 
    title = db.Column(db.String(100), nullable = False) #titles column
    status = db.Column(db.String(10), default = "pending") #status column

