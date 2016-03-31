"""
@author: Namita Maharanwar
created: Mar 29, 2016
CRUD Operations and some extra functions
Kind: Crew
"""

import datetime
import argparse

from utils.constants import get_dataset_id

import gcloud
from gcloud import datastore


def create_client():
    return gcloud.datastore.Client(get_dataset_id())

CLIENT = create_client()


def create_key(kind):
    key = CLIENT.key(kind)  # for primary key, an entity indentifier value
    return key


def add_crew(crew_details):
    """
    Adds a crew in the kind=Crews
    :param  crew_details: {
                "crew_name": "Visual Effects",
                "added_date": datetime.datetime.utcnow().strftime('%Y-%m-%d %h-%m-%s'),
                "user_id": "second"
            }
    :return type: <Key[{'kind': 'Crews', 'id': 5654313976201216L}], project=datastore1-1226>

    """

    print crew_details

    key = create_key('Crews')

    crew = datastore.Entity(key)

    crew.update(
        {
            "crew_name": crew_details["crew_name"][0],  # crew name (Like Sound team, visuals team etc)
            "added_date": datetime.datetime.utcnow().strftime('%Y-%m-%d %h-%m-%s'), # On which date it has got added.
            "user_id": crew_details["user_id"][0]   # to see who has added this
        }
    )
    CLIENT.put(crew)

    return crew.key


def get_crew(crew_id):
    """
    Returns a crew from Crews Kind
    :param crew_id: crew_id, the primary key to get the crew details.
    """
    crew_id = long(crew_id)
    key = CLIENT.key("Crews", crew_id)
    crew = CLIENT.get(key)


    if crew == None:
        return {
                'response_data': {
                    'message': "Crew {} does not exist.".format(crew_id)
                }
            }
    return dict(crew)

def get_all_crews():
    """
    Return all crews present in Kind=Crews.
    """
    query = CLIENT.query(kind='Crews')
    query.order = ['added_date']
    crews = query.fetch()
    if crews == None:
        return {
                'response_data': {
                    'message': "There are no concepts."
                }
            }
    all_crews = []
    all_list = list(query.fetch())
    for i in all_list:
        s = dict(i)
        s['id'] = i.__dict__['key'].id
        all_crews.append(s)

    return all_crews


def delete_crew(crew_id):
    """
    Returns a crew from Crews Kind
    :param crew_id: crew_id, the primary key to delete the crew details.
    """
    key = CLIENT.key('Crews', crew_id)
    crew = CLIENT.get(key)

    if not crew:
        raise ValueError(
                'Crew {} does not exist.'.format(crew_id)
            )
    CLIENT.delete(key)

    return {
            'response_data': {
                'is_deleted': True
            }
        }


def update_crew(crew_id, crew_details):
    """
    Returns a crew from Crews Kind
    :param crew_id: crew_id, the primary key to get the crew details.
    :param crew_details is the dict of fields to be edited.
    """
    key = CLIENT.key('Crews', crew_id)
    crew = CLIENT.get(key)

    if not crew:
        raise ValueError(
                'Concept {} does not exist.'.format(crew_id)
            )

    for column in crew_details.keys():
        crew[column] = crew_details[column]

    CLIENT.put(crew)

    return crew.key


if __name__ == "__main__":
    crew_details = {
        "crew_name": "Visual Effects",
        "added_date": datetime.datetime.utcnow().strftime('%Y-%m-%d %h-%m-%s'),
        "user_id": "second"
    }
    # print add_crew(crew_details)
    # x = 5076495651307520L
    # print get_crew(x)
    print get_all_crews()

