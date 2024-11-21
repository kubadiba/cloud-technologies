from app import db

class Gym(db.Model):
    __tablename__ = 'gym'
    gym_id = db.Column(db.Integer, primary_key=True)
    gym_name = db.Column(db.String(45), nullable=False)

    trainers = db.relationship('Trainer', backref='gym', lazy=True, cascade="all, delete-orphan")
    schedules = db.relationship('Schedule', backref='gym', lazy=True, cascade="all, delete-orphan")
    clients = db.relationship('Client', backref='gym', lazy=True, cascade="all, delete-orphan")

    def to_dict(self):
        return {"gym_id": self.gym_id, "gym_name": self.gym_name}

class Trainer(db.Model):
    __tablename__ = 'trainers'
    trainer_id = db.Column(db.Integer, primary_key=True)
    gym_id = db.Column(db.Integer, db.ForeignKey('gym.gym_id', ondelete="CASCADE"))
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(45))
    email = db.Column(db.String(45))
    specialization = db.Column(db.String(45))

    def to_dict(self):
        return {
            "trainer_id": self.trainer_id,
            "gym_id": self.gym_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "email": self.email,
            "specialization": self.specialization
        }

class Client(db.Model):
    __tablename__ = 'client'
    client_id = db.Column(db.Integer, primary_key=True)
    gym_id = db.Column(db.Integer, db.ForeignKey('gym.gym_id', ondelete="CASCADE"))
    name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    phone_number = db.Column(db.String(45))

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "gym_id": self.gym_id,
            "name": self.name,
            "last_name": self.last_name,
            "phone_number": self.phone_number
        }

class ClientProgram(db.Model):
    __tablename__ = 'client_programs'
    client_programs_id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            "client_programs_id": self.client_programs_id,
            "start_date": self.start_date,
            "end_date": self.end_date
        }

class Schedule(db.Model):
    __tablename__ = 'schedule'
    schedule_id = db.Column(db.Integer, primary_key=True)
    gym_id = db.Column(db.Integer, db.ForeignKey('gym.gym_id', ondelete="CASCADE"))
    day_of_week = db.Column(db.String(45))
    open_time = db.Column(db.Time)
    close_time = db.Column(db.Time)

    def to_dict(self):
        return {
            "schedule_id": self.schedule_id,
            "gym_id": self.gym_id,
            "day_of_week": self.day_of_week,
            "open_time": self.open_time,
            "close_time": self.close_time
        }
class WorkoutProgram(db.Model):
    __tablename__ = 'workout_programs'
    workout_programs_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        return {
            "workout_programs_id": self.workout_programs_id,
            "name": self.name,
            "description": self.description
        }

class ClientProgramWorkoutLink(db.Model):
    __tablename__ = 'client_programs_has_workout_programs'
    client_programs_id = db.Column(db.Integer, db.ForeignKey('client_programs.client_programs_id'), primary_key=True)
    workout_programs_id = db.Column(db.Integer, db.ForeignKey('workout_programs.workout_programs_id'), primary_key=True)

    # Встановлення зв’язків
    client_program = db.relationship("ClientProgram", backref="workouts")
    workout_program = db.relationship("WorkoutProgram", backref="clients")

    def to_dict(self):
        return {
            "client_programs_id": self.client_programs_id,
            "workout_programs_id": self.workout_programs_id
        }

