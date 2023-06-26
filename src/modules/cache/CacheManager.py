class CacheManager:
    def __init__(self):
        self._storage = []

    def reset(self):
        self._storage.clear()
    
    def add(self, key):
        if key not in self._storage:
            self._storage.append(key)

    def remove(self, key):
        if key in self._storage:
            self._storage.remove(key)

    def isExist(self, key):
        return key in self._storage
