from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.datastore_common import delete_concept


def handle_request(concept_id):
    concept = delete_concept(concept_id)
    return json.dumps(concept)
