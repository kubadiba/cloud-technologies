# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import yaml

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Swagger(app)

    # Завантаження конфігурації з YAML
    with open('app/config/app.yml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{config['database']['user']}:{config['database']['password']}"
        f"@{config['database']['host']}/{config['database']['name']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # 🟢 Підключаємо лише Trainer API
    from app.my_project.auth.route.trainer_route import trainer_bp
    app.register_blueprint(trainer_bp, url_prefix="/api")

    return app

