from flask import Flask
import psycopg2


app = Flask(__name__)
from views.views import *


if __name__ == "__main__":
    app.run(debug=True)
