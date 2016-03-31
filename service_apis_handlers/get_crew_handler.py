from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.db.crew import get_all_crews, get_crew


def handle_request(crew_id):
    if crew_id == 'all':
        crew = get_all_crews()
    else:
        crew = get_crew(crew_id)
    return json.dumps(crew)
