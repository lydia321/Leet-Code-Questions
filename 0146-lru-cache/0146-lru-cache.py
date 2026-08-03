class Node: 
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.Left,self.Right = Node(0,0), Node(0,0)
        self.Left.next = self.Right
        self.Right.prev = self.Left
    
    #remove from the list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
    #insert at the right
    def insert(self, node):
        prev = self.Right.prev
        prev.next = node
        node.prev = prev

        node.next = self.Right
        self.Right.prev = node
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        else: 
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.Left.next
                self.remove(lru)
                del self.cache[lru.key]

            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)