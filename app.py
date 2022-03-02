import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate1, identity1
from resources.user import UserRegister
from resources.item import Item, ItemsList
from resources.store import Store, StoreList

uri = os.getenv("DATABASE_URL")
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(uri, 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '123'
api = Api(app)

jwt = JWT(app, authenticate1, identity1)  # /auth

api.add_resource(Item, '/item/<string:name>')  # equal to @app.route('/Item/<string:name>)
api.add_resource(Store, '/store/<string:name>')

api.add_resource(ItemsList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
