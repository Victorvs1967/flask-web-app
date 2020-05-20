from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://victors:victor77@localhost/FlaskData'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'User {self.id}'
