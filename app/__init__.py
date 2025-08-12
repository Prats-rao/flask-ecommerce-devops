from flask import Flask
from .database import db
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'devsecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/ecommerce'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    return app
