import psycopg2
from flask_sqlalchemy import SQLAlchemy, Column, Integer, String, DateTime
from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://victors:victor77@localhost/FlaskData'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return '<h1>About app!</h1>'



class Data(db.Model):
    id = db.Column()


if __name__ == "__main__":
    app.run(debug=True)