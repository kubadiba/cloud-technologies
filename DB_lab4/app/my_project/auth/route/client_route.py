from flask import Blueprint, jsonify
from flasgger import swag_from
from app import db

client_bp = Blueprint('client_bp', __name__)

@client_bp.route('/api/clients', methods=['GET'])
@swag_from({
    'tags': ['Clients'],
    'summary': 'Отримати список клієнтів',
    'description': 'Повертає всіх клієнтів із бази даних (MySQL RDS)',
    'responses': {
        200: {
            'description': 'Успішна відповідь',
            'examples': {
                'application/json': [
                    {"id": 1, "name": "Olha", "age": 28},
                    {"id": 2, "name": "Taras", "age": 32}
                ]
            }
        }
    }
})
def get_clients():
    result = db.session.execute("SELECT client_id, name, age FROM client")
    clients = [{"id": r[0], "name": r[1], "age": r[2]} for r in result]
    return jsonify(clients)
