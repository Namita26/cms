"""
Create user apis like create any type of user
eg. creative director, producer, executive producer
"""

from flask import current_app as app
from flask import request
from flask_restful import Resource


def handle_request(request_details):
    print "get request handler"
    print request_details
    return request_details
