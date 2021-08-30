from flask import Blueprint
from flask_restx import Api
from app.portal.views import ItemsAPI

authorizations = {
    'Basic': {
        'type': 'Basic',
        'in': 'header',
        'name': 'Authorization',
    }
}

blueprint = Blueprint('portal', __name__)
api = Api(blueprint, security='Basic', authorizations=authorizations)

api.add_resource(ItemsAPI, '/items', endpoint='items', methods=['GET', 'PUT', 'POST', 'DELETE'])
