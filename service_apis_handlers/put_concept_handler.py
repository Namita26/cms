from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.db.concept import update_concept


def handle_request(concept_id, request_details):
    concept_id = update_concept(concept_id, request_details)
    return json.dumps({"message": str(concept_id) + "is edited"})
