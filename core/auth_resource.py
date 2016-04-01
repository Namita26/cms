from flask import Flask, render_template
from flask.ext import restful
from flask.ext.cors import CORS
from flask_restful import reqparse
from functools import wraps
from flask_restful import reqparse
from utils.db.users import is_valid_token



def authenticate(func):
    """
    TODO
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        cookies = parser.parse_args()
        token = cookies.get('token', "")
        is_authorized = is_valid_token(token) # select user from Users table where token=cookie_token

        is_valid = is_authorized['is_valid']
        if is_valid:
            response = func(*args, **kwargs)
            # print response
            return response
        restful.abort(401)
    return wrapper


class AuthResource(restful.Resource):
    method_decorators = [authenticate]
