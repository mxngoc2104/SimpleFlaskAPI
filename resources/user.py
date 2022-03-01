import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    # Get data from JSON using reqparse
    request_parser = reqparse.RequestParser()
    request_parser.add_argument('username',
                                type=str,
                                required=True,
                                help="This field can not be left blank!"
                                )

    request_parser.add_argument('password',
                                type=str,
                                required=True,
                                help="This field can not be left blank!"
                                )

    @classmethod
    def post(cls):
        request_data = cls.request_parser.parse_args()

        # check if user already exists
        user_check = UserModel.find_by_user_name(request_data['username'])
        if user_check:
            return {'message': "User already exists!"}, 400

        # Write data to database
        user = UserModel(**request_data)  # user = UserModel(request_data['username'], request_data['password'])
        user.save_to_db()

        # connection = sqlite3.connect(r'C:\Users\Ngoc\PycharmProjects\flaskProject_Section6\data.db')
        # cursor = connection.cursor()
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"  # NULL for auto-increment id
        # cursor.execute(query, (request_data['username'], request_data['password']))
        #
        # connection.commit()
        # connection.close()

        return {'message': "User created successfully!"}, 201
