class Node:
    def __init__ (self, key, val):
        self.key = key
        self.value = val
        self.next = self.prev = None

class LRUCache:
    """
    lru    1      2     mru
    none   10     20    none


    cache = {1:10, 2:20}
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # to get O(1) val : Node

        self.LRU = Node(0,0)
        self.MRU = Node(0,0)

        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU


    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev

        nextNode.prev = prevNode
        prevNode.next = nextNode


    def insertMRU(self, node):
        MRU = self.MRU.prev
        MRU.next = node
        node.prev = MRU

        self.MRU.prev = node
        node.next = self.MRU


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # update from curr pos to MRU
            self.remove(node)
            self.insertMRU(node)
            return node.value
        return -1
    

    def put(self, key: int, value: int) -> None:
        #1.  if insert an exisint one, update to MRU
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value) # update node value
        self.insertMRU(self.cache[key])

        # if bigger than capacity, delete the lru
        if len(self.cache) > self.capacity:
            LRUnode = self.LRU.next
            self.remove(LRUnode)
            # and remove in cache
            self.cache.pop(LRUnode.key)



