import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users(id int, username varchar(20), password varchar(20))"

cursor.execute(create_table)

user = ('1', 'ngoc', '123')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_query, user)

user = [
    ('2', 'bo', 'thanh'),
    ('3', 'me', 'hue')
]

cursor.executemany(insert_query, user)

connection.commit()

connection.close()