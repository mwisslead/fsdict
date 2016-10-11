'''Example of using fsdict to create a json file containing contents of a directory.'''

import sys
import json
import base64

from fsdict import FSDict

def decode_file(filename, data):
    try:
        return data.decode('UTF-8')
    except (AttributeError, UnicodeDecodeError):
        return base64.b64encode(data).decode('UTF-8')

def ignore(filename):
    if filename.endswith('.pyc'):
        return False
    elif filename.startswith('.'):
        return False
    elif filename == '__pycache__':
        return False
    return True

print(json.dumps(FSDict(sys.argv[1] if len(sys.argv) > 1 else None, read_func=decode_file, ignore_func=ignore), indent=4))
