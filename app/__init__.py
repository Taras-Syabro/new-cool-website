from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    bootstrap.init_app(app)

    from app.views import main_bp
    app.register_blueprint(main_bp)

    return app

