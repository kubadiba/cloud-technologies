# app/my_project/auth/route/trainer_route.py

from flask import Blueprint, jsonify, request
from flasgger import swag_from
from app import db
from app.my_project.auth.domain.gym_models import Trainer

# 🔹 створюємо blueprint без слова "_bp" у Swagger
trainer_bp = Blueprint('trainer', __name__)

# 🟦 GET — отримати всіх тренерів
@trainer_bp.route('/trainers', methods=['GET'])
@swag_from({
    'tags': ['Trainer'],
    'summary': 'Отримати всіх тренерів',
    'description': 'Повертає список усіх тренерів із бази даних.',
    'responses': {
        200: {
            'description': 'Успішна відповідь',
            'examples': {
                'application/json': [
                    {'id': 1, 'name': 'John Doe', 'specialization': 'Yoga'},
                    {'id': 2, 'name': 'Anna Smith', 'specialization': 'Cardio'}
                ]
            }
        }
    }
})
def get_trainers():
    trainers = Trainer.query.all()
    return jsonify([t.to_dict() for t in trainers])


# 🟩 POST — створити нового тренера
@trainer_bp.route('/trainers', methods=['POST'])
@swag_from({
    'tags': ['Trainer'],
    'summary': 'Додати нового тренера',
    'description': 'Створює нового тренера з вказаними даними.',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'example': {'name': 'John Doe', 'specialization': 'Yoga'}
            }
        }
    },
    'responses': {201: {'description': 'Тренера створено успішно'}}
})
def create_trainer():
    data = request.json
    trainer = Trainer(name=data['name'], specialization=data['specialization'])
    db.session.add(trainer)
    db.session.commit()
    return jsonify({'message': 'Trainer added successfully'}), 201


# 🟨 PUT — оновити тренера
@trainer_bp.route('/trainers/<int:id>', methods=['PUT'])
@swag_from({
    'tags': ['Trainer'],
    'summary': 'Оновити дані тренера',
    'description': 'Оновлює інформацію про тренера за ID.',
    'parameters': [{'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}],
    'responses': {200: {'description': 'Дані тренера оновлено'}}
})
def update_trainer(id):
    trainer = Trainer.query.get_or_404(id)
    data = request.json
    trainer.name = data.get('name', trainer.name)
    trainer.specialization = data.get('specialization', trainer.specialization)
    db.session.commit()
    return jsonify({'message': 'Trainer updated successfully'})


# 🟥 DELETE — видалити тренера
@trainer_bp.route('/trainers/<int:id>', methods=['DELETE'])
@swag_from({
    'tags': ['Trainer'],
    'summary': 'Видалити тренера',
    'description': 'Видаляє тренера з бази даних за вказаним ID.',
    'parameters': [{'name': 'id', 'in': 'path', 'required': True, 'type': 'integer'}],
    'responses': {200: {'description': 'Тренера видалено'}}
})
def delete_trainer(id):
    trainer = Trainer.query.get_or_404(id)
    db.session.delete(trainer)
    db.session.commit()
    return jsonify({'message': 'Trainer deleted successfully'})

