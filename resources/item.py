from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    # install request parser
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item need a store_id."
                        )

    # no need @app.route() here, using jwt_required for authentication instead
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': 'Item already existed'}

        data_request = Item.parser.parse_args()
        item = ItemModel(name, data_request['price'], data_request['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message': "An error occurred inserting the item"}, 500

        return item.json()

    # @jwt_required()
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': "Item deleted successfully"}

    # @jwt_required()
    def put(self, name):
        data_request = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item:
            try:
                item.price = data_request['price']
                item.store_id = data_request['store_id']
            except:
                return {'message': 'An error occurred'}, 500
        else:
            try:
                item = ItemModel(name, data_request['price'], data_request['store_id'])
            except:
                return {'message': 'An error occurred'}, 500

        item.save_to_db()
        return item.json()


class ItemsList(Resource):
    def get(self):
        return {'item': [item.json() for item in ItemModel.query.all()]}
        # ANOTHER WAY: return {'item': list(map(lambda x: x.json(), ItemModel.query.all()))}

        # item = []
        # connection = sqlite3.connect('../data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items"
        # result_query = cursor.execute(query)
        # for row in result_query:
        #     item.append({'name': row[1], 'price': row[2]})
        #
        # connection.close()
        # return {'items': item}
