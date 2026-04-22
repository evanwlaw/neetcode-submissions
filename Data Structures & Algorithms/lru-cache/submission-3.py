class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    doubly linked list. 
    node -> key, val, prev, next

    (0,0)               (0,0)
    lru                 mru
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0,0)  # dummy left of lru
        self.right = Node(0,0)  #dummy right of mru
        self.cache = {}  # key : node

        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        """
        prev -> next
        node
        next -> prev
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    
    def insert(self, node):
        """
        insert as MRU before self.right dummy node
        """
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node

        node.next, node.prev = nxt, prev



    def get(self, key: int) -> int:
        # get from cache if in it
        if key in self.cache:
            # remove the node
            self.remove(self.cache[key])
            # insert/update to MRU
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1      
        

    def put(self, key: int, value: int) -> None:
        # update if it exists
        if key in self.cache:
            # remove node
            self.remove(self.cache[key])

        # add node if new or update val
        self.cache[key] = Node(key, value)

        # add/update as MRU
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


