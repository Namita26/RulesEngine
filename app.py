from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask.ext import restful

from apis.events_api import RulesAPIHandler
from models.events import db

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost/cube"
db.init_app(app)

api.add_resource(RulesAPIHandler, '/api/rules')

if __name__ == '__main__':
  
  app.run(host="0.0.0.0")
  
