from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
def initapp():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    with app.app_context():
        db.create_all()

    from app.index import bp as index_bp
    app.register_blueprint(index_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.register import bp as reg_bp
    app.register_blueprint(reg_bp)
    return app

from app import model
