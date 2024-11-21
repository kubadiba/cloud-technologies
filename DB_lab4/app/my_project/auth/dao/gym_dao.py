from app import db
from app.my_project.auth.domain.gym_models import (Gym, Trainer, Client
,Schedule, ClientProgram, WorkoutProgram,ClientProgramWorkoutLink)

class GymDAO:
    @staticmethod
    def get_all():
        return Gym.query.all()

    @staticmethod
    def create(gym_data):
        gym = Gym(**gym_data)
        db.session.add(gym)
        db.session.commit()
        return gym

    @staticmethod
    def update(gym_id, gym_data):
        gym = Gym.query.get(gym_id)
        if gym:
            for key, value in gym_data.items():
                setattr(gym, key, value)
            db.session.commit()
            return gym
        return None


    @staticmethod
    def delete(gym_id):
        gym = Gym.query.get(gym_id)
        if not gym:
            return False  # Gym не знайдено
        db.session.delete(gym)
        db.session.commit()
        return True


    @staticmethod
    def get_client_program_workouts():
        return ClientProgramWorkoutLink.query.all()

    @staticmethod
    def add_client_program_workout(link_data):
        link = ClientProgramWorkoutLink(**link_data)
        db.session.add(link)
        db.session.commit()
        return link

class TrainerDAO:
    @staticmethod
    def get_all():
        return Trainer.query.all()

    @staticmethod
    def create(trainer_data):
        trainer = Trainer(**trainer_data)
        db.session.add(trainer)
        db.session.commit()
        return trainer

class ClientDAO:
    @staticmethod
    def get_all():
        return Client.query.all()

    @staticmethod
    def create(client_data):
        client = Client(**client_data)
        db.session.add(client)
        db.session.commit()
        return client
    @staticmethod
    def get_clients_by_gym(gym_id):
        return Client.query.filter_by(gym_id=gym_id).all()


class ScheduleDAO:
    @staticmethod
    def get_all():
        return Schedule.query.all()

    @staticmethod
    def create(schedule_data):
        schedule = Schedule(**schedule_data)
        db.session.add(schedule)
        db.session.commit()
        return schedule

class ClientProgramDAO:
    @staticmethod
    def get_all():
        return ClientProgram.query.all()
    @staticmethod
    def get_client_program_workouts():
        return db.session.query(ClientProgramWorkoutLink).all()

    @staticmethod
    def create(program_data):
        program = ClientProgram(**program_data)
        db.session.add(program)
        db.session.commit()
        return program
    @staticmethod
    def add_client_program_workout(client_programs_id, workout_programs_id):
        try:
            new_link = ClientProgramWorkoutLink(
                client_programs_id=client_programs_id,
                workout_programs_id=workout_programs_id
            )
            db.session.add(new_link)
            db.session.commit()
            return new_link
        except Exception as e:
            print(f"Error adding client_program_workout link: {e}")
            db.session.rollback()
            return None

class WorkoutProgramDAO:
    @staticmethod
    def get_all():
        return WorkoutProgram.query.all()

    @staticmethod
    def create(program_data):
        program = WorkoutProgram(**program_data)
        db.session.add(program)
        db.session.commit()
        return program
