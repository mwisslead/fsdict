from __future__ import print_function

import os
import errno
import logging

LOGGER = logging.getLogger('fsdict')
DEBUG = LOGGER.debug

class FSDict(dict):
    def __init__(self, basedir=None, read_func=None, write_func=None, ignore_func=None):
        if basedir is None:
            basedir = '.'
        try:
            basedir = os.path.abspath(basedir)
        except AttributeError:
            raise TypeError('Cannot convert {} to pathname.'.format(basedir))
        if os.path.isfile(basedir):
            raise TypeError('FSDict cannot be created from file')
        self.basedir = basedir
        if read_func:
            self.read_func = read_func
        if write_func:
            self.write_func = write_func
        if ignore_func:
            self.ignore_func = ignore_func

    def _build_path(self, filepath):
        if filepath is None:
            return self.basedir
        try:
            filepath = os.path.join(self.basedir, filepath)
            if self.basedir != os.path.abspath(os.path.dirname(filepath)):
                raise KeyError('{} is not in {}'.format(filepath, self.basedir))
            return filepath
        except AttributeError:
            raise TypeError('Cannot convert {} to pathname.'.format(filepath))

    def read_func(self, filepath):
        with open(filepath) as fid:
            return fid.read()

    def __getitem__(self, filepath):
        filepath = self._build_path(filepath)
        if os.path.isfile(filepath):
            return self.read_func(filepath)
        return FSDict(filepath, self.read_func, self.write_func, self.ignore_func)

    def write_func(self, filepath, output):
        if not hasattr(output, 'decode'):
            raise TypeError('Can\'t write {} to file'.format(repr(output)))
        dirpath = os.path.dirname(filepath)
        DEBUG('creating directories: {}'.format(filepath))
        try:
            os.makedirs(dirpath)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(dirpath):
                pass
            else:
                raise
        with open(filepath, 'wb') as fid:
            fid.write(output)

    def __setitem__(self, filepath, val):
        filepath = self._build_path(filepath)
        if val is None and os.path.isfile(filepath):
            os.remove(filepath)
            return
        if val is None and os.path.isdir(filepath):
            os.rmdir(filepath)
            return
        self.write_func(filepath, val)

    def force_delete(self, key):
        try:
            self[key] = None
        except OSError:
            if isinstance(self[key], FSDict):
                for path in self[key]:
                    try:
                        self[key].force_delete(path)
                    except OSError:
                        pass
                self[key] = None
                return
            raise

    def __repr__(self):
        return 'FSDict({})'.format(repr(self.basedir))

    def __iter__(self):
        return (key for key in self.keys())

    def __len__(self):
        return len(self.keys())

    def iteritems(self):
        return ((key, self[key]) for key in self.keys())
        
    def items(self):
        return self.iteritems()

    def ignore_func(self, filepath):
        return True

    def keys(self):
        try:
            return [key for key in os.listdir(self.basedir) if self.ignore_func(key)]
        except OSError:
            return []
