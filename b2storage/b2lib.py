# Copyright George Sibble 2018

import os
from b2_exceptions import B2ApplicationKeyNotSet, B2KeyIDNotSet, B2InvalidBucketName, B2InvalidBucketConfiguration
from b2_exceptions import B2BucketCreationError
from connector import B2Connector

from objects.bucket import B2Bucket
from objects.bucket_list import B2Buckets

class B2(object):

    def __init__(self, key_id=None, application_key=None):
        if key_id is None or application_key is None:
            key_id = os.environ.get('B2_KEY_ID', None)
            application_key = os.environ.get('B2_APPLICATION_KEY', None)
        if key_id is None:
            raise B2KeyIDNotSet
        if application_key is None:
            raise B2ApplicationKeyNotSet
        self.key_id = key_id
        self.application_key = application_key
        self.connector = B2Connector(key_id=self.key_id, application_key=self.application_key)


    @property
    def buckets(self):
        return B2Buckets(connector=self.connector)
