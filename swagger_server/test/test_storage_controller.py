# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.storage_object import StorageObject
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestStorageController(BaseTestCase):
    """ StorageController integration test stubs """

    def test_get_storage(self):
        """
        Test case for get_storage

        Get a return of all storage arrays
        """
        response = self.client.open('/v1/storage',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
