from . import db
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True,primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    