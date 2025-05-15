from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.String(20))
    name = db.Column(db.String(150))
    type = db.Column(db.String(100))
    ownership = db.Column(db.String(100))
    emergency_services = db.Column(db.String(10))
    rating = db.Column(db.String(20))
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    state = db.Column(db.String(2))
    zip_code = db.Column(db.Integer)
