from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
flask_bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

import backend.views