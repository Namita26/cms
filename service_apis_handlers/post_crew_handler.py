from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.db.crew import add_crew


def handle_request(request_details):
    crew_id = add_crew(request_details)
    return json.dumps({"message": str(crew_id) + "is created"})
