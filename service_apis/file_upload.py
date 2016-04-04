import json
from flask import request
from flask import current_app as app
from flask_restful import reqparse, abort, Api, Resource
from service_apis_handlers import post_concept_handler, put_concept_handler, get_concept_handler, delete_concept_handler
import requests
from werkzeug import secure_filename
import os
from utils.cloud_store_utils import upload_object
from utils.general import generate_random_string


class FileUpload(Resource):

    def post(self):
        file = request.files['file']

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        app.logger.info('Received request for Concept support file upload')
        destination_filepath = "concept/" + generate_random_string(10) + "/" + filename
        x = upload_object(
            "datastore1-1226.appspot.com",
            os.path.join(app.config['UPLOAD_FOLDER'], filename),
            destination_filepath
        )
        return json.dumps({"google_store_file_path": x['mediaLink']})
