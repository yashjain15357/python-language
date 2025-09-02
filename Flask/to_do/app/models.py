# here we define database schema 
# table structrue

from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default="Pending")


class User(db.Model):
    user_id=db.Column(db.Integer , primary_key=True)
    user_name=db.Column(db.String(100), nullable=False)
    user_email=db.Column(db.String(100), nullable=False)
    user_password=db.Column(db.String(20) , nullable = False)