class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    """
    
    left -> lru ..  ..  .. mru -> left

    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.cache = {} # val : Node(key)

        self.left.next = self.right
        self.right.prev = self.left

    def remove_node(self, node):
        """
        prev >< node >< next
        """
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert_mru(self,node):
        """
        prev >< node >< right
        """
        prev, nxt = self.right.prev, self.right

        prev.next = nxt.prev = node

        node.next, node.prev = nxt, prev



    def get(self, key: int) -> int:
        if key in self.cache: 
            # remove node and insert as MRU
            self.remove_node(self.cache[key])
            self.insert_mru(self.cache[key])
            return self.cache[key].val
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert_mru(self.cache[key])

        # if cap, revoke lru
        if self.cap < len(self.cache):
            lru = self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]


        
