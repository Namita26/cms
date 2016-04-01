"""
Created flask app
"""

from flask import Flask, render_template
from flask.ext import restful
from flask.ext.cors import CORS
from service_apis.users import User
from service_apis.concept import Concept, ConceptList, EmbededLink
from service_apis.file_upload import FileUpload
from service_apis.auth import Auth
from service_apis.crew import Crew, CrewList

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True

UPLOAD_FOLDER = '/home/namita/work/cms/concept_uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

api = restful.Api(app)

api.add_resource(User, '/')
api.add_resource(ConceptList, '/concept')
api.add_resource(Concept, '/concept/<string:concept_id>')
api.add_resource(Auth, '/auth/')
api.add_resource(EmbededLink, '/embeded_link/')
api.add_resource(FileUpload, '/file_upload')
api.add_resource(Crew, '/crew/<string:crew_id>')
api.add_resource(CrewList, '/crew')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
