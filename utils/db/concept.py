"""
created: Mar 8, 2016

CRUD operations
Kind: Concept
"""


import datetime
import argparse

from utils.constants import get_dataset_id

import gcloud
from gcloud import datastore


def create_client():
    return gcloud.datastore.Client(get_dataset_id())

CLIENT = create_client()


def create_key(kind, primary_key):
    key = CLIENT.key(kind, primary_key)  # for primary key, an entity indentifier value
    return key


def add_concept(concept_details):

    key = create_key('Concepts', 'fifth')

    concept = datastore.Entity(
            key, exclude_from_indexes=['concept_note'])

    print "\n---------------In add concept----------------\n"
    print concept_details
    print "\n-----------------\n"

    concept.update({
        'created': datetime.datetime.utcnow().strftime('%Y-%m-%d %h-%m-%s'),
        'concept_title': concept_details['concept_title'][0],
        'producer': concept_details['producer'][0],
        'talent': concept_details['talent'][0],
        'no_of_videos': concept_details['no_of_videos'][0],
        'concept_note': concept_details['concept_note'],
        'shoot_days': concept_details['shoot_days'][0],
        'talent_costs': concept_details['total_budget'][0],
        'set_and_art': concept_details['set_and_art'][0],
        'crew': concept_details['crew'][0],
        'total_budget': concept_details['total_budget'][0],
        'file_storage_url': concept_details['file_storage_url'][0],
        'embeded_links': concept_details['embeded_links'],
        'status': concept_details['status'][0]
    })

    CLIENT.put(concept)

    return concept.key


def update_concept(concept_id, concept_details):
    key = CLIENT.key('Concepts', concept_id)
    concept = CLIENT.get(key)

    print "*****************\n\n", concept_details
    print "*****************\n\n"
    if not concept:
        raise ValueError(
                'Concept {} does not exist.'.format(concept_id)
            )

    for column in concept_details.keys():
        concept[column] = concept_details[column]

    CLIENT.put(concept)

    return concept.key

def get_all_concepts():
    query = CLIENT.query(kind='Concepts')
    query.order = ['created']
    concepts = query.fetch()
    if concepts == None:
        return {
                'response_data': {
                    'message': "There are no concepts."
                }
            }
    all_concepts = []
    all_list = list(query.fetch())
    for i in all_list:
        s = dict(i)
        s['name'] = i.__dict__['key'].name
        all_concepts.append(s)

    return all_concepts

def get_concept(concept_id):
    key = CLIENT.key('Concepts', concept_id)
    concept = CLIENT.get(key)
    if concept == None:
        return {
                'response_data': {
                    'message': "Concept {} does not exist.".format(concept_id)
                }
            }
    return dict(concept)


def delete_concept(concept_id):
    key = CLIENT.key('Concepts', concept_id)
    concept = CLIENT.get(key)

    if not concept:
        raise ValueError(
                'Concept {} does not exist.'.format(concept_id)
            )
    CLIENT.delete(key)

    return {
            'response_data': {
                'is_deleted': True
            }
        }
