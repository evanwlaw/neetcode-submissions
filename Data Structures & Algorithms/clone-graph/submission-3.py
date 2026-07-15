"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        1 : 2
        2 : 1, 3
        3 : 2
        '''
        nodeMap = {}

        def dfs(node: Optional['Node']):
            if node in nodeMap:
                return nodeMap[node]
            
            node_copy = Node(node.val)
            nodeMap[node] = node_copy

            # make copies of neighbors to the copied node
            for nei in node.neighbors:
                node_copy.neighbors.append(dfs(nei))
            return node_copy
        return dfs(node) if node else None