"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph (self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
	
        def dfs(oldNode):
            if oldNode in nodeMap:
                return nodeMap[oldNode]
            cloneNode = Node(oldNode.val)
            nodeMap[oldNode] = cloneNode

            for nei in oldNode.neighbors:
                cloneNode.neighbors.append(dfs(nei))
            return cloneNode
            
        return 	dfs(node) if node else None
