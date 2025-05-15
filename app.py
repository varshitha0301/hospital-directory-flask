from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospitals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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

def load_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        with open("hospitals.csv", newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                hospital = Hospital(
                    hospital_id=row["hospital_id"],
                    name=row["name"],
                    type=row["type"],
                    ownership=row["ownership"],
                    emergency_services=row["emergency_services"],
                    rating=row["rating"],
                    address=row["address"],
                    city=row["city"],
                    state=row["state"],
                    zip_code=row["zip_code"]
                )
                db.session.add(hospital)
            db.session.commit()

@app.route('/')
def index():
    selected_state = request.args.get('state')
    states = db.session.query(Hospital.state).distinct().order_by(Hospital.state).all()
    states = [s[0] for s in states]

    if selected_state:
        hospitals = Hospital.query.filter_by(state=selected_state).limit(100).all()
    else:
        hospitals = Hospital.query.limit(100).all()

    return render_template('index.html', hospitals=hospitals, states=states, selected_state=selected_state)

@app.route('/hospital/<int:id>')
def hospital_detail(id):
    hospital = Hospital.query.get_or_404(id)
    return render_template('hospital_detail.html', hospital=hospital)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    load_data()
    app.run(host='0.0.0.0', port=8000, debug=True)
