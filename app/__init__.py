from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
# from app import views
# from app import error

# def create_app(config_name):
#     app=Flask(__name__)
#     bootstrap=Bootstrap(app)
#     app.config.from_object(config_options[config_name])


#     from .main import main  as main_blueprint
#     app.register_blueprint(main_blueprint)

#     from .requests import configure_request
#     configure_request(app)


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap = Bootstrap(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
