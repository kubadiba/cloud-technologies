# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger       # ✅ додай цей імпорт
import yaml

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    Swagger(app)                   # ✅ активуй Swagger тут

    # Завантаження конфігурації з app.yml
    with open('app/config/app.yml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{config['database']['user']}:{config['database']['password']}"
        f"@{config['database']['host']}/{config['database']['name']}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ініціалізація бази даних
    db.init_app(app)

    # Імпорт та реєстрація маршрутів
    from app.my_project.auth.route.gym_route import register_routes
    register_routes(app)
    from app.my_project.auth.route.trainer_route import trainer_bp
    from app.my_project.auth.route.client_route import client_bp
    from app.my_project.auth.route.gym_route import gym_bp
    from app.my_project.auth.route.schedule_route import schedule_bp

    app.register_blueprint(trainer_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(gym_bp)
    app.register_blueprint(schedule_bp)

    return app

