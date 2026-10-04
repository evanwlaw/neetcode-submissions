"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
        
        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]
            
            new_node = Node(node.val)
            nodeMap[node] = new_node
            
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            return new_node
            
        
        return dfs(node) if node else None
        
        