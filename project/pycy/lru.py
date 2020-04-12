from collections import OrderedDict


class LRUCache(object):
    def __init__(self, length):
        self.length = length
        self.cache = OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.length:
                self.cache.popitem(last=False)
        self.cache[key] = value
