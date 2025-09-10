from flask import Flask,blueprints
from flask_sqlalchemy import  SQLAlchemy


db = SQLAlchemy()
def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = "TO_DO_KEY"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.galary import galary_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(galary_bp)

    return app
