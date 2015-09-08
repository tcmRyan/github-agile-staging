from flask import Flask
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
flask_bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

import backend.views
from backend.models import Vendor