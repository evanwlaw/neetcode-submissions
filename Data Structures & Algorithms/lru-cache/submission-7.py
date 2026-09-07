class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    """
    capacity = 2

    L_end (LRU)                                  R_end (MRU)
    null                                        null        
        node:1 val:10  <> node:2 val:20 
    
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = Node(0,0)      
        self.MRU = Node(0,0)      
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU

        self.cache = {} # intkey : node
    
    # prevNode <> node <> nextNode
    #   prevNode <> nextNode
    def remove(self, node):
        nextNode = node.next
        prevNode = node.prev

        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    #   currNode <> MRU (end node)
    #   currNode <> newNode <> MRU (end node)
    def insert(self, node):
        currNode = self.MRU.prev
        currNode.next = node
        node.prev = currNode

        self.MRU.prev = node
        node.next = self.MRU


    def get(self, key: int) -> int:
        if key in self.cache:
            # update lru
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        # update values if exisiting by first removing node
        if key in self.cache:
            self.remove(self.cache[key])

        # update lru (if it exists, it's bumped to MRU)
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity: # eject LRU
            LRU = self.LRU.next
            self.remove(LRU)
            del self.cache[LRU.key]



        
