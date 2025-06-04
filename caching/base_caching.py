# base_caching.py

class BaseCaching:
    """ Base class for caching systems """

    def __init__(self):
        """ Initialize the cache dictionary """
        self.cache_data = {}

    def print_cache(self):
        """ Print the current contents of the cache """
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
