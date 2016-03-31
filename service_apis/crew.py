"""
@author: Namita Maharanwar
@created: Mar, 2016
All REST methods for <Kind - Crews>.
"""

import json
from flask import request
from flask import current_app as app
from flask_restful import reqparse, abort, Api, Resource
from service_apis_handlers import get_crew_handler, post_crew_handler, delete_crew_handler, put_crew_handler
import requests
from werkzeug import secure_filename
import os


class Crew(Resource):

    def get(self, crew_id):
        """
        This method returns a Crew using crew_id passed in the request
        """
        app.logger.debug('Received get crew request: %s',
            crew_id)

        return get_crew_handler.handle_request(crew_id)

    def delete(self, crew_id):
        """
        This method SHOULD archieve the crew :P
        """
        #TODO
        app.logger.debug('Received crew deletion request: %s',
            crew_id)

        return delete_crew_handler.handle_request(long(crew_id))


    def put(self, crew_id):
        """
        This method edits a crew using paramters passed in the request
        """
        to_be_edited = dict(request.form)
        app.logger.info('Received request for crew editing with '+ crew_id + 'fields')

        return put_crew_handler.handle_request(long(crew_id), to_be_edited)

class CrewList(Resource):

    def get(self):
        """
        This method returns all crews from Kind Crew
        """
        app.logger.debug('Received get all crews request')
        return get_crew_handler.handle_request(crew_id="all")

    def post(self):
        """
        This method adds crew to Kind Crew
        """
        app.logger.debug('Received post request for Crew')
        return post_crew_handler.handle_request(dict(request.form))

