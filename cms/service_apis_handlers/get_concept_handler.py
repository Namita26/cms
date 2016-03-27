from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.datastore_common import get_all_concepts, get_concept


def handle_request(concept_id):
    if concept_id == 'all':
        concept = get_all_concepts()
    else:
        concept = get_concept(concept_id)
    return json.dumps(concept)
