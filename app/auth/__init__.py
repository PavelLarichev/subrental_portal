from flask import Blueprint
from flask_restx import Api
from app.auth.views import LoginAPI

authorizations = {
    'Basic': {
        'type': 'Basic',
        'in': 'header',
        'name': 'Authorization',
    }
}

blueprint = Blueprint('auth', __name__)
api = Api(blueprint, security='Basic', authorizations=authorizations)

api.add_resource(LoginAPI, '/login', endpoint='login', methods=['POST', 'PUT'])
