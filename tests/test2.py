from syncs3 import LocalObjectCache
import os

bucket_name = bucket_name
prefix = prefix_name
obj = LocalObjectCache(bucket_name, prefix)

filename__ = file_name
key = os.path.abspath(filename__)

def test_with_params():
    try:
        assert obj.upload_obj(key) == key
    except FileNotFoundError as e:
        print('File Not found.')

def test_without_params():
    try:
        assert obj.download_obj() == key
    except FileNotFoundError as e:
        print('File Not found.')
