import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
api = Api(app)
CORS(app)


Secret_Key = os.environ.get("SECRET_KEY")
Database_Uri = os.environ.get("SQLALCHEMY_DATABASE_URI")

app.config["SECRET_KEY"] = Secret_Key
app.config["SQLALCHEMY_DATABASE_URI"] = Database_Uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

from apis.main import home

app.register_blueprint(home)
