from syncs3 import LocalObjectCache
import os

bucket_name = 'bucketname'
prefix = 'prefix'
obj = LocalObjectCache(bucket_name, prefix)
filename__ = 'filename'
key = os.path.join(obj.prefix, filename__)
tag = tag_value
def test_with_params():
    try:
        assert obj.download_obj(key, tag) == key, tag
    except FileNotFoundError as e:
        print('File Not found.')

def test_without_params():
    try:
        assert obj.download_obj() == key, tag
    except FileNotFoundError as e:
        print('File Not found.')
