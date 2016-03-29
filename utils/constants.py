
project_meta_data = {
    "APPS_DOMAIN_NAME": "glamrs.com",
    "CLIENT_ID": "816284744569-hblbg79baprfv7472kopc7q0ql53bn9b.apps.googleusercontent.com",
    "DATASET_ID": "datastore1-1226"
}

def get_app_domain_name():
    return project_meta_data.get('APPS_DOMAIN_NAME')


def get_client_id():
    return project_meta_data.get('CLIENT_ID')

def get_dataset_id():
    return project_meta_data.get('DATASET_ID')
