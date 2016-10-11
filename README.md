# fsdict
dictionary-like access to the filesystem

usage:
```
    >>> from fsdict import FSDict
    >>> def file_decode(filename, data):
    ...     return eval(data.decode('UTF-8'))
    ... 
    >>> def file_encode(filename, data):
    ...     return repr(data).encode('UTF-8')
    ... 
    >>> def ignore(filename):
    ...     return filename.endswith('.txt')
    ... 
    >>> dirdict = FSDict('.', read_func=file_decode, write_func=file_encode, ignore_func=ignore)
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
