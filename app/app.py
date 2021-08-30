from flask import Flask
from flask_restx import Api
from app.extentions import ma, db, bcrypt
from app.auth import api as auth_module
from app.portal import api as portal_module
from config import config

def start_service():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    # api = Api(app)


    app.register_blueprint(auth_module.blueprint, url_prefix='/auth')
    app.register_blueprint(portal_module.blueprint, url_prefix='/portal')

    return app