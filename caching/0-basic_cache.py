# 0-basic_cache.py

from base_caching import BaseCaching  

class BasicCache(BaseCaching):
    """ Basic caching system that inherits from BaseCaching """

    def put(self, key, item):
        """
        Add an item to the cache.
        If either key or item is None, do nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item  

    def get(self, key):
        """
        Retrieve an item by key.
        Return None if key is None or doesn't exist.
        """
        if key is None:
            return None
        return self.cache_data.get(key)  # Return the value or None
