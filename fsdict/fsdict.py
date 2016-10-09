from __future__ import print_function

import os
import logging

LOGGER = logging.getLogger('fsdict')
DEBUG = LOGGER.debug

class FSDict(object):
    def __init__(self, basedir=None):
        if basedir is None:
            self.basedir = '.'
        else:
            self.basedir = basedir

    def _build_path(self, filepath):
        if self.basedir and filepath:
            filepath = os.path.join(self.basedir, filepath)
        elif self.basedir:
            filepath = self.basedir
        return filepath

    def __getitem__(self, filepath):
        filepath = self._build_path(filepath)
        if os.path.isfile(filepath):
            with open(filepath, 'rb') as fid:
                data = fid.read()
            return data
        return FSDict(filepath)

    def __setitem__(self, filepath, val):
        filepath = self._build_path(filepath)
        dirpath = os.path.dirname(filepath)
        DEBUG('creating directories: {}'.format(filepath))
        try:
            os.makedirs(dirpath)
        except OSError:
            pass
        with open(filepath, 'wb') as fid:
            fid.write(val)

    def __repr__(self):
        return 'FSDict({})'.format(repr(self.basedir))

    def __iter__(self):
        if self.basedir and os.path.isdir(self.basedir):
            return (item for item in os.listdir(self.basedir))
        return (self[None] for i in range(0))

    def __len__(self):
        return 1

    def iteritems(self):
        if self.basedir and os.path.isdir(self.basedir):
            return ((item, self[item]) for item in os.listdir(self.basedir))
        return (('', self[none]) for i in range(0))
        
    def items(self):
        return self.iteritems()
