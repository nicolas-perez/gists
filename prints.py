from pprint import pprint

def utf8ize(data):
        """Recursively encodes every string in utf-8."""
        if isinstance(data, dict):
            dict_ = {}
            for (k, v) in data.iteritems():
                dict_[str(k)] = utf8ize(v)
            return dict_
        elif isinstance(data, list):
            list_ = []
            for el in data:
                list_.append(utf8ize(el))
            return list_
        elif isinstance(data, unicode) or isinstance(data, str):
            return data.encode('utf-8')
        else:
            return data

def prints(data):
    """Prints data (list or dict) without the ugly u prefixes in Python 2.

    Example:
    >>> d = {u'a': u'b', u'c': 'd', 'e': [u'f', 'g', 5]}
    >>> print(d)
    {u'a': u'b', u'c': 'd', 'e': [u'f', 'g', 5]}
    >>> prints(d)
    {'a': 'b', 'c': 'd', 'e': ['f', 'g', 5]}
    """
    print(utf8ize(data))

def pprints(data):
    """Same as prints but uses pprint instead of print."""
    pprint(utf8ize(data))