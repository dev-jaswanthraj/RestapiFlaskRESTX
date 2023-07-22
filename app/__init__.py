from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["JWT_SECRET_KEY"] = "H! there Its Jaswanthraj R ;)"

# DB
db = SQLAlchemy(app)

# API
api = Api(app)

# JWT
jwt = JWTManager(app)

with app.app_context():
    from app.models import ImportTestTable, TestTable
    db.create_all()

from app import views

        
