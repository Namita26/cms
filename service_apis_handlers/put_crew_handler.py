from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.db.crew import update_crew


def handle_request(crew_id, request_details):
    crew_id = update_crew(crew_id, request_details)
    return json.dumps({"message": str(crew_id) + "is edited"})
