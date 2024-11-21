from flask import Blueprint, jsonify, request
from app.my_project.auth.service.gym_service import GymService, TrainerService, ClientService, ScheduleService, \
    ClientProgramService, WorkoutProgramService

gym_controller = Blueprint('gym_controller', __name__)

# Routes for Gym
@gym_controller.route('/gyms', methods=['GET'])
def get_gyms():
    gyms = GymService.get_all_gyms()
    return jsonify([gym.to_dict() for gym in gyms])

@gym_controller.route('/gyms', methods=['POST'])
def create_gym():
    data = request.json
    gym = GymService.create_gym(data)
    return jsonify(gym.to_dict()), 201

@gym_controller.route('/gyms/<int:gym_id>', methods=['PUT'])
def update_gym(gym_id):
    print(f"PUT request received for gym_id={gym_id} with data={request.json}")
    data = request.json
    gym = GymService.update_gym(gym_id, data)
    if gym:
        return jsonify(gym.to_dict()), 200
    return jsonify({"error": "Gym not found"}), 404

@gym_controller.route('/gyms/<int:gym_id>', methods=['DELETE'])
def delete_gym(gym_id):
    print(f"DELETE request received for gym_id={gym_id}")
    result = GymService.delete_gym(gym_id)
    if result:
        return jsonify({"message": "Gym deleted successfully"}), 200
    return jsonify({"error": "Gym not found"}), 404


# Routes for Trainers
@gym_controller.route('/trainers', methods=['GET'])
def get_trainers():
    trainers = TrainerService.get_all_trainers()
    return jsonify([trainer.to_dict() for trainer in trainers])

@gym_controller.route('/trainers', methods=['POST'])
def create_trainer():
    data = request.json
    trainer = TrainerService.create_trainer(data)
    return jsonify(trainer.to_dict()), 201

# Routes for Clients
@gym_controller.route('/clients', methods=['GET'])
def get_clients():
    clients = ClientService.get_all_clients()
    return jsonify([client.to_dict() for client in clients])

@gym_controller.route('/clients', methods=['POST'])
def create_client():
    data = request.json
    client = ClientService.create_client(data)
    return jsonify(client.to_dict()), 201

# Routes for Schedule
@gym_controller.route('/schedules', methods=['GET'])
def get_schedules():
    schedules = ScheduleService.get_all_schedules()
    return jsonify([schedule.to_dict() for schedule in schedules])

@gym_controller.route('/schedules', methods=['POST'])
def create_schedule():
    data = request.json
    schedule = ScheduleService.create_schedule(data)
    return jsonify(schedule.to_dict()), 201

# Routes for Client Programs
@gym_controller.route('/client_programs', methods=['GET'])
def get_client_programs():
    programs = ClientProgramService.get_all_programs()
    return jsonify([program.to_dict() for program in programs])

@gym_controller.route('/client_programs', methods=['POST'])
def create_client_program():
    data = request.json
    program = ClientProgramService.create_program(data)
    return jsonify(program.to_dict()), 201

# Routes for Workout Programs
@gym_controller.route('/workout_programs', methods=['GET'])
def get_workout_programs():
    programs = WorkoutProgramService.get_all_programs()
    return jsonify([program.to_dict() for program in programs])

@gym_controller.route('/workout_programs', methods=['POST'])
def create_workout_program():
    data = request.json
    program = WorkoutProgramService.create_program(data)
    return jsonify(program.to_dict()), 201




@gym_controller.route('/client_programs_workouts', methods=['GET'])
def get_client_program_workouts():
    links = ClientProgramService.get_client_program_workouts()
    detailed_links = [
        {
            "client_program": link.client_program.to_dict(),
            "workout_program": link.workout_program.to_dict()
        }
        for link in links
    ]
    return jsonify(detailed_links)

@gym_controller.route('/client_programs_workouts', methods=['POST'])
def add_client_program_workout():
    data = request.json
    new_link = ClientProgramService.add_client_program_workout(data)
    if new_link:
        return jsonify(new_link.to_dict()), 201
    return jsonify({"error": "Failed to create link"}), 400


@gym_controller.route('/gyms/<int:gym_id>/clients', methods=['GET'])
def get_clients_by_gym(gym_id):
    clients = ClientService.get_clients_by_gym(gym_id)
    if clients:
        return jsonify([client.to_dict() for client in clients]), 200
    return jsonify({"error": "No clients found for this gym"}), 404
