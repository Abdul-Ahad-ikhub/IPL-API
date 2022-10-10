#Module importing ,features
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask
from apis import api
from db import db
from flask_sqlalchemy import SQLAlchemy





#Configuration 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Mysql786@localhost/scenario2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER_UI_JSONEDITOR'] = True
db = SQLAlchemy(app)
db.init_app(app)
api.init_app(app)

app.run(debug=True)