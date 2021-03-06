import json
from flask import request
from flask import current_app as app
from flask_restful import reqparse, abort, Api, Resource
from service_apis_handlers import post_concept_handler, put_concept_handler, get_concept_handler, delete_concept_handler
import requests
from werkzeug import secure_filename
import os
from core.auth_resource import authenticate


class ConceptList(Resource):
    method_decorators = [authenticate]

    def get(self):
        """
        This method edits a Concept using paramters passed in the request
        """
        app.logger.debug('Received get all concepts request')
        return get_concept_handler.handle_request({"concept_id": "all", "useremail": request.args.get("useremail", "")})

    def post(self):
        """
        This method creates Concept using paramters passed in the request
        """

        app.logger.info('Received request for Concept creation')

        return post_concept_handler.handle_request(dict(request.form))

class Concept(Resource):
    method_decorators = [authenticate]

    def get(self, concept_id):
        """
        This method returns a Concept using concept_id passed in the request
        """
        app.logger.debug('Received get concept request: %s',
            concept_id)

        return get_concept_handler.handle_request(concept_id)

    def delete(self, concept_id):
        """
        This method SHOULD archieve the concept :P
        """
        #TODO
        app.logger.debug('Received concept deletion request: %s',
            concept_id)

        return delete_concept_handler.handle_request(long(concept_id))

    def put(self, concept_id):
        """
        This method edits a Concept using paramters passed in the request
        """
        to_be_edited = dict(request.form)
        app.logger.info('Received request for Concept editing with '+ concept_id + 'fields')

        return put_concept_handler.handle_request(concept_id, to_be_edited)


class EmbededLink(Resource):

    def get(self):
        """
        This method edits a Concept using paramters passed in the request
        """
        link = request.args["url"]

        result = requests.get("https://www.youtube.com/oembed?url="+link)
        app.logger.debug('Received get EmbededLink request: %s', link)
        embeded_link = "<link>" + result.json()['html'] + "</link>"
        dict1 = {"embeded_link": embeded_link}
        return json.dumps(dict1)
