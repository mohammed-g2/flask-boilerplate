from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from config import cfg_options

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(cfg_name: str):
    app = Flask(__name__)
    app.config.from_object(cfg_options[cfg_name])

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    login_manager.init_app(app)

    # import blueprints

    # for testing purposes
    @app.route('/')
    def index():
        return render_template('layout.html')

    return app
