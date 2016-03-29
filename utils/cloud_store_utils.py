import argparse
import json

from googleapiclient import discovery
from googleapiclient import http
from oauth2client.client import GoogleCredentials
from utils.general import generate_random_string


def create_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('storage', 'v1', credentials=credentials)


def upload_object(bucket, source_filepath, destination_filepath):
    service = create_service()

    # This is the request body as specified:
    # http://g.co/cloud/storage/docs/json_api/v1/objects/insert#request
    body = {
        'name': destination_filepath,

    }

    # Now insert them into the specified bucket as a media insertion.
    # http://g.co/dev/resources/api-libraries/documentation/storage/v1/python/latest/storage_v1.objects.html#insert
    with open(source_filepath, 'rb') as f:
        req = service.objects().insert(
            bucket=bucket, body=body,
            # You can also just set media_body=filename, but # for the sake of
            # demonstration, pass in the more generic file handle, which could
            # very well be a StringIO or similar.
            predefinedAcl="publicRead",
            media_body=http.MediaIoBaseUpload(f, 'application/octet-stream'))
        resp = req.execute()

    print resp
    return resp


def get_object(bucket, filename, out_file):
    service = create_service()

    # Use get_media instead of get to get the actual contents of the object.
    # http://g.co/dev/resources/api-libraries/documentation/storage/v1/python/latest/storage_v1.objects.html#get_media
    req = service.objects().get_media(bucket=bucket, object=filename)

    http.MediaIoBaseDownload
    downloader = http.MediaIoBaseDownload(out_file, req)

    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download {}%.".format(int(status.progress() * 100)))

    return out_file


def delete_object(bucket, filename):
    service = create_service()

    req = service.objects().delete(bucket=bucket, object=filename)
    resp = req.execute()
    print resp
    return resp


if __name__ == "__main__":
    upload_object("datastore1-1226.appspot.com", "/home/namita/Pictures/sample_fb_explorer.png", "/concept/test/sample_fb_explorer.png")

    # with open("/home/namita/work/cms/out.txt", "w") as f:
    #     get_object("datastore1-1226.appspot.com", "namita.test", f)

    # delete_object("datastore1-1226.appspot.com", "file1.txt")
