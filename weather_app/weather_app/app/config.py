import os
class BaseConfiguration:
    TESTING = False
    OPEN_WEATHER_API_TOKEN = '9debd7baf39598dc162af95a8e9a7b86'
class DevelopmentConfig(BaseConfiguration):
    DEBUG = True
    ENV = 'dev'
    TEMPLATES_AUTO_RELOAD = True

class ProductionConfig(BaseConfiguration):
    DEBUG = False
    TESTING = True
    ENV = 'production'

config = {
    'dev': 'app.config.DevelopmentConfig',
    'prod': 'app.config.ProductionConfig'
}

def configure_app(app):
    """ Configure the Flask WSGI Instance according the enviroment Variable FLASK_CONF """
    enviroment = os.getenv('FLASK_CONFIG', 'dev')
    app.config.from_object(config[enviroment])
    # configure_error_handlers(app)

# def configure_error_handlers(app):
#     @app.errorhandler(404)
#     def not_found(err):
#         return render_template('not_found/page_not_found.html'), 404

