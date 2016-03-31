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


def add_user(user_details):
    """
    Adds a user in the kind=Users
    :param  user_details: {
                "user_name": "Visual Effects",
                "added_date": datetime.datetime.utcnow().strftime('%Y-%m-%d %h-%m-%s'),
                "user_id": "second"
            }
    :return type: <Key[{'kind': 'users', 'id': 5654313976201216L}], project=datastore1-1226>

    """

    print user_details

    key = create_key('Users')

    user = datastore.Entity(key)

    user.update(
        {
            "fname": user_details["f_name"][0],  # fname
            "lname": user_details["l_name"][0],  # lname
            "taken_timestamp": datetime.datetime.utcnow().strftime('%Y-%m-%d %h-%m-%s'),
            "email_verified": user_details["email_verified"][0],
            "email": user_details['email'][0],
            "role": user_details['role'][0],
            "token": []
        }
    )
    CLIENT.put(user)

    return user.key


def get_all_users():
    """
    Return all crews present in Kind=Crews.
    """
    query = CLIENT.query(kind='Users')
    query.order = ['taken_timestamp']
    users = query.fetch()
    if users == None:
        return {
                'response_data': {
                    'message': "There are no users."
                }
            }
    all_users = []
    all_list = list(query.fetch())
    for i in all_list:
        s = dict(i)
        s['id'] = i.__dict__['key'].id
        all_users.append(s)

    return all_users


def get_user(email, token):
    """
    Returns a crew from Users Kind
    :param email: email id, propery to get the user details.
    """
    query = CLIENT.query(kind='Users')
    query.add_filter("email", "=", email)
    user_details = {}
    for user in list(query.fetch()):
        user_details = dict(user)
        user_details['id'] = user.__dict__['key'].id
    print "\n--------------------\n"
    print user_details
    print "\n--------------------\n"
    if user_details == {}:
        return False
    else:
        if token not in user_details.get("token", []):
            existing_tokens = user_details.get("token", [])
            existing_tokens.append(token)
            user_details['token'] = existing_tokens
            # update user
            key = CLIENT.key('Users', user_details['id'])
            user_to_be_updated = CLIENT.get(key)
            for column in user_details.keys():
                user_to_be_updated[column] = user_details[column]
            CLIENT.put(user_to_be_updated)
        return True


def is_valid_token(token):
    """
    Checks if the token is valid or not
    :param token: Google Identifier Platform token taken from input request cookie.
    :return_type:
    """
    user_email = False
    print "\n\n=-------------------In token Validation------------\n\n"
    query = CLIENT.query(kind='Users')
    query.add_filter("token", "=", token)
    for user in list(query.fetch()):
        user_email = dict(user)['email']
    if user_email:
        print "YEs----------------------"
        return {"is_valid": True, "email": user_email}
    else:
        return {"is_valid": False}

if __name__ == "__main__":
    user_details = {
        "f_name": ["Arnosh"],
        "l_name": ["Bodhanwala"],
        "email": ["arnosh@glamrs.com"],
        "email_verified": ["yes"],
        "role": ["Admin"]
    }
    print add_user(user_details)
    # print get_all_users()
