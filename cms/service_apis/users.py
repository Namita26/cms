"""
Create user apis like create any type of user
eg. creative director, producer, executive producer
"""

import json
from flask import current_app as app
from flask import request
from flask_restful import Resource
from service_apis_handlers import get_users_handler

class User(Resource):

    def get(self):
        """
        This method is used to fetch all registered users
        """
        request_details = {}
        request_details = json.loads(request.args.get('content'))
        get_users_handler.handle_request(request_details)
        return request_details

    """
    def is_authorised(role, category, permissionn):
        if self.is_logged_in():
            return True
        return False
    """
