#My Simple REST API
## Installation
```angular2html
pip install Flask
pip install Flask-RESTful
pip install Flask-SQLAlchemy
#run app
python app.py
```
## Description
By using Flask framework, I have created a REST API connected to local database to store
information of things like items and stores. It can retrieve data from JSON file and used
for storing or returning on user demands. <br />
Also for authenticate, I used JSON Web Token (JWT). This API provides an endpoint for user to register,
and these private information will be stored in database. After that, they can use their username
and password for the authorization.

## Implementation
This project is implemented using Flask RESTful, SQLAlchemy, JSON Web Token (JWT).
It is a REST API for a store.

## Author
Written by Mai Xuan Ngoc
