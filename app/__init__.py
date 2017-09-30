#import os
from flask import Flask
#from flask_pymongo import PyMongo
from app.user_models import *
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

myApp = Flask(__name__)
myApp.config['MONGO_DBNAME'] = 'my_db'
myApp.config['SECRET_KEY'] = 'secret^!@#$%^&key_ForSession.maneGement^'
#mongo = PyMongo(myApp)
db = MongoEngine(myApp)

login_manager = LoginManager()
login_manager.init_app(myApp)


@login_manager.user_loader
def user_loader(user_id):
    """Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.objects.get(id=user_id)