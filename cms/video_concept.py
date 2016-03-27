from datetime import datetime
import time
from all_exceptions.exceptions import MyException
from users import User


class VideoConcept:

    def __init__(self, concept_id=None, fields):
        if concept_id:
            self.concept_id = concept_id
        else:
            self.concept_id = time.time()

        self.fields = fields

    @staticmethod
    def create(concept, user):
        err_msg = ''
        if user.is_authorised(role='producer', category=self.fields['category'], permission='create'):
            if self.fields['title'] != None:
                return self.concept_id
            else:
                err_msg = 'No title provided'
                raise MyException('Could not create the concept: ' + err_msg)
