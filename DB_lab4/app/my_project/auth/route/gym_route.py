
from app.my_project.auth.controller.gym_controller import gym_controller

def register_routes(app):
    """
    Register all routes for the gym management module.
    """
    app.register_blueprint(gym_controller, url_prefix='/api')


from flask import Blueprint, jsonify
from flasgger import swag_from
from app import db

gym_bp = Blueprint('gym_bp', __name__)

@gym_bp.route('/api/gyms', methods=['GET'])
@swag_from({
    'tags': ['Gyms'],
    'summary': 'Отримати всі спортзали',
    'description': 'Повертає перелік філіалів спортклубу з бази даних (MySQL RDS)',
    'responses': {
        200: {
            'description': 'Успішна відповідь',
            'examples': {
                'application/json': [
                    {"id": 1, "gym_name": "FitZone Lviv"},
                    {"id": 2, "gym_name": "PowerLife Kyiv"}
                ]
            }
        }
    }
})
def get_gyms():
    result = db.session.execute("SELECT gym_id, gym_name FROM gym")
    gyms = [{"id": r[0], "gym_name": r[1]} for r in result]
    return jsonify(gyms)
