from flask import Flask
from app.config import configure_app

def create_app():
    """ Instance and create a Flask WSGI App """
    app = Flask(__name__, static_folder=None)
    configure_app(app)

    with app.app_context():
        from app.weather import weather_bp
        app.register_blueprint(weather_bp)

    return app