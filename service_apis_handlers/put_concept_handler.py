from flask import current_app as app
from flask import request
from flask_restful import Resource
import json
from utils.db.concept import update_concept


def handle_request(concept_id, request_details):

    print request_details
    
    modified_request_details = {
        'status': request_details['status'][0],
        'set_and_art': request_details['set_and_art'][0],
        'talent': request_details['talent'][0],
        'producer': request_details['producer'][0],
        'video_names': request_details['video_names'][0],
        'concept_title': request_details['concept_title'][0],
        'no_of_videos': request_details['no_of_videos'][0],
        'crew': list(set(request_details['crew'][0].split(","))),
        'shoot_days': request_details['shoot_days'][0],
        'concept_note': request_details['concept_note'][0],
        'total_budget': request_details['total_budget'][0],
        'embeded_links': request_details['embeded_links'],
        'talent_costs': request_details['talent_costs'][0]
    }

    concept_id = update_concept(concept_id, modified_request_details)
    return json.dumps({"message": str(concept_id) + "is edited"})
