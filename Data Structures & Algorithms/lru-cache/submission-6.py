class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None		

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        
        # initialize double linked list
        self.left = Node(0,0) # initialize dummy node 
        self.right = Node(0,0) # initialize dummy node 
        self.left.next = self.right
        self.right.prev = self.left

        # hashmap of cache ( key : Node(key,value))
        self.cache = {}


    def remove(self, node):
        '''
        prev <> node <> next → prev <> next
        '''
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


    def insert_mru(self, node):
        '''
        prev_node <> self.right (MRU ptr) → prev_node <> new node <> self.right
        '''
        prev_node = self.right.prev
        
        prev_node.next = node
        node.prev = prev_node

        node.next = self.right
        self.right.prev = node
        

    def get(self, key):
        if key in self.cache:
            # remove node from linkedlist as we want to promote it to MRU
            node = self.cache[key]
            self.remove(node)
                
            #insert node as MRU (right side of linkedlist)
            self.insert_mru(node)

            return node.val

        return -1 # key is not in cache


    def put(self, key, value):
        # if key exists, update value:
        if key in self.cache:
            # remove node from linkedlist as we want to promote it to MRU
            self.remove(self.cache[key])
            
        # add into hashmap
        self.cache[key] = Node(key, value)
            
        # insert node as MRU (right side of linkedlist)
        self.insert_mru(self.cache[key])

        # check if hashmap is at capacity. And remove LRU if over capacity
        if len(self.cache) > self.capacity:
        # remove node at LRU (left side of linkedlist)
            lru_node = self.left.next
            self.remove(lru_node)
            
            # delete from cache hashmap
            del self.cache[lru_node.key]
