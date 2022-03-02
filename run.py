from db import db
from app import app


# create tables using SQLAlchemy
@app.before_first_request
def create_tables():
    db.create_all()


# call init_app outside 'main' for fixing Heroku problem
db.init_app(app)
