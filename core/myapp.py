"""
Created flask app
"""

from flask import Flask, render_template
from flask.ext import restful
from service_apis.users import User
from service_apis.concept import Concept, ConceptList, EmbededLink
from service_apis.file_upload import FileUpload
from service_apis.auth import Auth
from flask.ext.cors import CORS


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


def authenticate(func):
    """
    TODO
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        #is_authorized = check_token_from_cookie()
        is_authorized = True
        if is_authorized:
            return func(*args, **kwargs)
        restful.abort(401)
    return wrapper


class AuthResource(restful.Resource):
    method_decorators = [authenticate]

if __name__ == "__main__":
    app.run(host='0.0.0.0')
