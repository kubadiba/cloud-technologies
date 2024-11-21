
from app.my_project.auth.controller.gym_controller import gym_controller

def register_routes(app):
    """
    Register all routes for the gym management module.
    """
    app.register_blueprint(gym_controller, url_prefix='/api')
