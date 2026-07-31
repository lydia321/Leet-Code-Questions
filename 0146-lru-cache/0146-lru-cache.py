class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.LRU.remove(key)
        self.LRU.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.LRU.remove(key)
            self.LRU.append(key)
        else:
            if self.capacity == len(self.cache):
                last_idx = self.LRU.pop(0)
                self.cache.pop(last_idx)
            self.LRU.append(key)
            self.cache[key]=value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)