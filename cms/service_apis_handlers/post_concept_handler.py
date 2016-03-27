from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.datastore_common import add_concept


def handle_request(request_details):
    concept_id = add_concept(request_details)
    return json.dumps({"message": str(concept_id) + "is created"})
