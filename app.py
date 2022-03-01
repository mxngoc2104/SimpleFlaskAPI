from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate1, identity1
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '123'
api = Api(app)


# create tables using SQLAlchemy
@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate1, identity1)  # /auth

api.add_resource(Item, '/item/<string:name>')  # equal to @app.route('/Item/<string:name>)
api.add_resource(Store, '/store/<string:name>')

api.add_resource(ItemsList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)