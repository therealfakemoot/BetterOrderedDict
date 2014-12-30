from collections import MutableMapping


class BetterOrderedDict(MutableMapping):
    def __init__(self, **kwargs):
        self._d = dict()
        self._keys = []

    def __len__(self):
        return len(self._d)

    def __iter__(self):
        for key in self._keys:
            yield key

    def __setitem__(self, key, value):
        self._keys.append(key)
        self._d[key] = value

    def __getitem__(self, key):
        return self._d[key]

    def __delitem__(self, key):
        self._keys.remove(key)
        del self._d[key]

    def key_index(self, key):
        return self._keys.index(key)

    def insert(self, key, value, index):
        if key in self._keys:
            self._keys.remove(key)
        self._keys.insert(index, key)
        self._d[key] = value

    def reorder_keys(self, keys):
        if self._keys != self._d:
            raise ValueError('Keys do not match.')
        self._keys = keys

    def __repr__(self):
        return str([(key, self[key]) for key in self])
