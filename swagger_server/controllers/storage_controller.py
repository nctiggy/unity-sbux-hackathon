import connexion
from swagger_server.models.storage_object import StorageObject
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from couchdb_storage import Couch_storage

couch_params = {
            "hostname": "localhost",
            "port": 5984,
            "dbName": "storage"
            }


def get_storage_array():
    """
    Get a return of all storage arrays
    This endpoint will return a list From couchDB

    :rtype: StorageObject
    """
    return 'do some magic!'


def new_storage_array(body):
    """
    Create a new stroage array entry
    This enpoint will create a new storage array entry in couchdb
    :param body: Storage array details to be added to the entry
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = StorageObject.from_dict(connexion.request.get_json())
    couchdb = Couch_storage.new(couch_params)
    couchdb.createNew(body)
