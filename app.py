from flask import Flask,jsonify,make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db,Bird
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
api = Api(app)

migrate = Migrate(app,db)
db.init_app(app)


class Birds(Resource):
    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds),200)
    
api.add_resource(Birds, '/birds')
