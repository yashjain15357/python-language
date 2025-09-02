from flask import Flask
from flask_sqlalchemy import SQLAlchemy # help to talk with data base

# create database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "TO_DO_KEY"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    from app.routes.auth import auth_bp
    from app.routes.task import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app