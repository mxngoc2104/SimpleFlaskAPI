from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name=name LIMIT 1
        # connection = sqlite3.connect(r'C:\Users\Ngoc\PycharmProjects\flaskProject_Section6\data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(row[1], row[2])

    def save_to_db(self):  # Do both insert and update
        db.session.add(self)
        db.session.commit()
        # connection = sqlite3.connect(r'C:\Users\Ngoc\PycharmProjects\flaskProject_Section6\data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES (NULL,?,?)"
        # cursor.execute(query, (self.name, self.price))
        # query = "UPDATE items " \
        #         "SET price = ? " \
        #         "WHERE name = ?"
        # cursor.execute(query, (self.price, self.name,))
        #
        # connection.commit()
        # connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
