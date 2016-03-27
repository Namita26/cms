import traceback
import unittest
from login import VideoConcept, User

class Concept(unittest.TestCase):

    """
    Testcases for Concept creation
    """

    # check the user's role and if the role permits the desired action then only pass otherwise fail.

    def setUp(self):
        self.user = User(1, 'namita', 'goyal', 'namita@glamrs.com')


    def test_concept_id_normal(self):
        result = VideoConcept(1, 'skin', 'some title', 'some note', 123, 12, ['Shruti']).save(self.user)
        self.assertEqual(result,
                        True,
                        "Need concept ID, it should not be none")
    def test_concept_title_none(self):
        result = VideoConcept(1, 'skin', None, 'some note', 123, 12, ['Shruti']).save(self.user)
        self.assertNotEqual(result,
                        False,
                        "Need title, it should not be none")
    
    def test_concept_title_blank(self):
        result = VideoConcept(1, 'skin', '', 'some note', 123, 12, ['Shruti']).save(self.user)
        self.assertNotEqual(result,
                        'Need title',
                        "Need title, it should not be blank")
    
    def test_concept_title_non_str(self):
        result = VideoConcept(1, 'skin', 11, 'some note', 123, 12, ['Shruti']).save(self.user)
        self.assertNotEqual(result,
                        'title should not be int',
                        "Concept title should be string")
    
    def test_concept_correct_note(self):
        result = VideoConcept(1, 'skin', 'some title', 'some note', 123, 12, ['Shruti']).save(self.user)
        self.assertEqual(result,
                        True,
                        "Concept Note is not up to the mark")
    
    def test_concept_note_none(self):
        result = VideoConcept(1, 'skin', 'some title', None, 123, 12, ['Shruti']).save(self.user)
        self.assertNotEqual(result,
                        False,
                        "Concept Note should not be blank")
    
    def test_concept_category_none(self):
        result = VideoConcept(1, None, 'some title', 'some note', 123, 12, ['Shruti']).save(self.user)
        self.assertNotEqual(result,
                        False,
                        "Concept Category should not be None")

if __name__ == "__main__":
    unittest.main()

