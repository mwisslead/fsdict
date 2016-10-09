'''Example of using fsdict to create a json file containing contents of a directory.'''

import sys
import json
import base64

from fsdict import FSDict

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        retval = {}
        for filename in o:
            try:
                try:
                    retval[filename] = o[filename].decode('UTF-8')
                except (AttributeError, UnicodeDecodeError):
                    retval[filename] = base64.b64encode(o[filename])
            except TypeError:
                retval[filename] = o[filename]
        return retval

print(json.dumps(FSDict(sys.argv[1] if len(sys.argv) > 1 else None), indent=4, cls=MyEncoder))
