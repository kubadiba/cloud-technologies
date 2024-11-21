# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml

# Ініціалізація об'єкта SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Завантаження конфігурації з app.yml
    with open('app/config/app.yml', 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{config['database']['user']}:{config['database']['password']}@{config['database']['host']}/{config['database']['database']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ініціалізація бази даних
    db.init_app(app)

    # Імпорт та реєстрація маршрутів
    from app.my_project.auth.route.gym_route import register_routes
    
    register_routes(app)

    return app
