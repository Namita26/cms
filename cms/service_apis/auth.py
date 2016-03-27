from oauth2client import client, crypt
from flask import current_app as app
from flask import request
import flask
from flask_restful import abort, Resource
import json
from utils.constants import get_app_domain_name, get_client_id
# from service_apis_handlers import store_user


USERS = [
    "namita@glamrs.com",
    "arnosh@glamrs.com"
]


class Auth(Resource):

    def get(self):
        print "In get--------------------\n\n"
        APPS_DOMAIN_NAME = get_app_domain_name()

        CLIENT_ID = get_client_id()

        token = request.args.get('id_token')
        print token, "-----------------------\n"
        idinfo = client.verify_id_token(token, CLIENT_ID)
        print idinfo

        if 'glamrs.com' not in idinfo['email']:
            abort(401, message="The "+ idinfo['email'] + "is not an authorised user.")

        # store_user.handle_request(idinfo)
        return idinfo
