from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from 
class dball:
    def __init__(self, db, DB_NAME, app):
        self.db = db
        self.DB_NAME= DB_NAME
        self.app= app
    db = SQLAlchemy()
    DB_NAME = "database.db"
    def  create_app(self):
        app = Flask(__name__) # just initializing flask 
        app.config['SECRET_KEY'] = 'fadfafdfdfas jlkjl ' # this is going to encrypt or secure the cookies or session data related to our web site
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{self.DB_NAME}'
        self.db.init_app(app)
        from website.view import viewall as view
        from website.auth import Logall as auth
    
    
        app.register_blueprint(view, url_prefix='/')
        app.register_blueprint(auth, url_prefix='/')

        from .models import User, Note
        create_database(app)

        return app

    def create_database(self):
        if not path.exists ('website/' + self.DB_NAME):
            self.db.create_all(app=self.app)
            print ("Created Database! ")
            return 'Created Database!'