import json

from flask import request
from flask_restx import Resource
from app.extentions import bcrypt
from app.auth.models import Users


class LoginAPI(Resource):
    """
    Метод для создания пользователя в системе
    """
    def put(self, *args, **kwargs):
        request_params = json.loads(request.data)
        if not request_params:
            return 'No input data provided', 400
        login = request_params.get('login')
        password = request_params.get('password')
        email = request_params.get('email')
        pw_hash = bcrypt.check_password_hash(password, 10)
        new_user = Users()
        new_user.create(login=login, email=email, password=pw_hash)
        return 'ok', 200

    """
    Метод для регистрации пользователя в системе
    """
    def post(self, *args, **kwargs):
        request_params = json.loads(request.data)
        login = request_params.get('login')
        user = Users.get(login=login)
        if user:
            pswd_check = bcrypt.check_password_hash(user.password, request_params['password'])
            if pswd_check:
                return {'login': login}, 200
            else:
                return 'Invalid password', 401
