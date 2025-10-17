from flask import Blueprint, jsonify
from flasgger import swag_from
from app import db
from app.my_project.auth.domain.gym_models import Schedule
schedule_bp = Blueprint('schedule_bp', __name__)

@schedule_bp.route('/api/schedules', methods=['GET'])
@swag_from({
    'tags': ['Schedule'],
    'summary': 'Отримати розклад тренувань',
    'description': 'Повертає розклад усіх занять у спортзалі (MySQL RDS)',
    'responses': {
        200: {
            'description': 'Успішна відповідь',
            'examples': {
                'application/json': [
                    {"id": 1, "day": "Monday", "trainer": "John Doe", "client": "Olha"},
                    {"id": 2, "day": "Tuesday", "trainer": "Jane Smith", "client": "Taras"}
                ]
            }
        }
    }
})
def get_schedule():
    result = db.session.execute("""
        SELECT schedule_id, day_of_week, trainer_id, client_id
        FROM schedule
    """)
    schedules = [
        {"id": r[0], "day": r[1], "trainer_id": r[2], "client_id": r[3]}
        for r in result
    ]
    return jsonify(schedules)
