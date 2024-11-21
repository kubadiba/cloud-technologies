from app.my_project.auth.dao.gym_dao import (GymDAO, TrainerDAO, ClientDAO, ScheduleDAO,
ClientProgramDAO, WorkoutProgramDAO)

class GymService:
    @staticmethod
    def get_all_gyms():
        return GymDAO.get_all()

    @staticmethod
    def create_gym(gym_data):
        return GymDAO.create(gym_data)

    @staticmethod
    def update_gym(gym_id, gym_data):
        return GymDAO.update(gym_id, gym_data)

    @staticmethod
    def delete_gym(gym_id):
        return GymDAO.delete(gym_id)

    @staticmethod
    def get_client_program_workouts():
        return GymDAO.get_client_program_workouts()

    @staticmethod
    def add_client_program_workout(link_data):
        return GymDAO.add_client_program_workout(link_data)


class TrainerService:
    @staticmethod
    def get_all_trainers():
        return TrainerDAO.get_all()

    @staticmethod
    def create_trainer(trainer_data):
        return TrainerDAO.create(trainer_data)

class ClientService:
    @staticmethod
    def get_all_clients():
        return ClientDAO.get_all()
    @staticmethod
    def get_clients_by_gym(gym_id):
        return ClientDAO.get_clients_by_gym(gym_id)
    @staticmethod
    def create_client(client_data):
        return ClientDAO.create(client_data)


class ScheduleService:
    @staticmethod
    def get_all_schedules():
        return ScheduleDAO.get_all()

    @staticmethod
    def create_schedule(schedule_data):
        return ScheduleDAO.create(schedule_data)

class ClientProgramService:
    @staticmethod
    def get_all_programs():
        return ClientProgramDAO.get_all()
    @staticmethod
    def add_client_program_workout(data):
        client_programs_id = data.get("client_programs_id")
        workout_programs_id = data.get("workout_programs_id")
        return ClientProgramDAO.add_client_program_workout(client_programs_id, workout_programs_id)
    @staticmethod
    def create_program(program_data):
        return ClientProgramDAO.create(program_data)
    @staticmethod
    def get_client_program_workouts():
        return ClientProgramDAO.get_client_program_workouts()
class WorkoutProgramService:
    @staticmethod
    def get_all_programs():
        return WorkoutProgramDAO.get_all()

    @staticmethod
    def create_program(program_data):
        return WorkoutProgramDAO.create(program_data)
