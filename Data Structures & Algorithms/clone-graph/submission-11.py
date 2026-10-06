"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Need deep copy

        given a node. need to traverse it

        we can dfs from the node.
            each time we dfs, we need to check if we've seen it before (e.g. detect cycles)
            - could use a hashmap where each node returns the new copy
            - if in hashmap, it means we've created a copy before. so return that new copy
            dfs through neighbors
        """

        newNodeMap = {} # node : newNode


        def dfs(node):
            if node in newNodeMap:
                return newNodeMap[node] # return the new copy version
            
            # create the new copy node and in the map
            newCopy = Node(node.val)
            newNodeMap[node] = newCopy

            for nei in node.neighbors:
                newNodeMap[node].neighbors.append(dfs(nei))
            return newCopy
        if not node:
            return None
        return dfs(node)