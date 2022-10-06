from syncs3 import LocalObjectCache
import os

obj = LocalObjectCache('sentientx', 'EOD/')
__filename__ = 'feather_512.fth'
key = os.path.join(obj.prefix, __filename__)
tag = "'hello'"
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
