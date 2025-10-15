from flask import Blueprint, jsonify
from flasgger import swag_from

trainer_bp = Blueprint('trainer_bp', __name__)

@trainer_bp.route('/api/trainers', methods=['GET'])
@swag_from({
    'tags': ['Trainers'],
    'summary': 'Отримати всіх тренерів',
    'description': 'Повертає список тренерів із бази даних (MySQL на RDS)',
    'responses': {
        200: {
            'description': 'Успішна відповідь',
            'examples': {
                'application/json': [
                    {"id": 1, "name": "John Doe", "specialization": "Yoga"},
                    {"id": 2, "name": "Jane Smith", "specialization": "Fitness"}
                ]
            }
        }
    }
})
def get_trainers():
    result = db.session.execute("SELECT trainer_id, name, specialization FROM trainers")
    trainers = [
        {"id": row[0], "name": row[1], "specialization": row[2]}
        for row in result
    ]
    return jsonify(trainers)
