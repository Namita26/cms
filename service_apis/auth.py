from oauth2client import client, crypt
from flask import current_app as app
from flask import request
import flask
from flask_restful import abort, Resource
import json
from utils.constants import get_app_domain_name, get_client_id
# from service_apis_handlers import store_user
from utils.db.users import get_user


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
        idinfo = client.verify_id_token(token, CLIENT_ID)
        print idinfo
        if 'glamrs.com' not in idinfo['email']:
        # if 'glamrs.com' != idinfo['hd']:
            abort(401, message="The "+ idinfo['email'] + "is not an authorised user.")
        else:
            if get_user(idinfo["email"], token):
                response = flask.Response(idinfo)
                # response.set_cookie('token',value=token)
                # response.set_cookie('user_email',value=idinfo['email'])
                return response
            else:
                abort(401, message="The "+ idinfo['email'] + "is not an authorised user.")
