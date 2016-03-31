from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.db.crew import delete_crew


def handle_request(crew_id):
    crew = delete_crew(crew_id)
    return json.dumps(crew)
