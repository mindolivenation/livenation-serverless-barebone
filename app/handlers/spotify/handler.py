"""Spotify worker
@author mindosilalahi@livenation.com
"""
import boto3
from app.libraries.dal import DataAccessLayer

DATA_ACCESS_LAYER = DataAccessLayer()

def run_spotify_worker(event, context):
    """Lambda handler for executing spotify worker

    Arguments:
        event {dict} -- event dict
        context {object} -- lambda context

    Returns:
        dict -- sample response
    """
    print('Begin spotify worker')
    return {
        'statusCode': 200,
        'body': 'Successfully executing this method',
        'payload': {
            'credential': DATA_ACCESS_LAYER.get_access_credential()
        }
    }
