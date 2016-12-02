# fsdict
dictionary-like access to the filesystem

usage:
```
    >>> from fsdict import FSDict
    >>> def file_read(filename):
    ...     with open(filename, 'rb') as fid:
    ...         return eval(fid.read().decode('UTF-8'))
    ... 
    >>> def file_write(filename, data):
    ...     with open(filename, 'wb') as fid:
    ...         fid.write(repr(data).encode('UTF-8'))
    ... 
    >>> def ignore(filename):
    ...     return filename.endswith('.txt')
    ... 
    >>> dirdict = FSDict('.', read_func=file_read, write_func=file_write, ignore_func=ignore)
    >>> dirdict.keys()
    []
    >>> dirdict['textfile.txt'] = u'Lorem ipsum dolor sit amet.'
    >>> dirdict['number.txt'] = 5
    >>> dirdict.keys()
    ['number.txt', 'textfile.txt']
    >>> dirdict['textfile.txt']
    'Lorem ipsum dolor sit amet.'
    >>> dirdict['number.txt']
    5

```

see fstojson.py for an example
