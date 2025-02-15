

from . import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(50),nullable=False)
    phone = db.Column(db.String(10), nullable=False)




