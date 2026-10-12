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
        dfs to traverse graph

        neighbors is list of nodes connected (bi directional)

        Input: adjList = [[2],[1,3],[2]]
        Output: [[2],[1,3],[2]]

        so in example, if we dfs to node 3, the neighbor in node 3 is 2. since we traversed and saw node three, we should terminate (e.g. return the new copied)
         
        visited to count for cycles -> {} node : cloned node

        """

        visited = {} # node : cloned node

        def dfs(node):
            if not node:
                return None
            
            if node in visited:
                return visited[node] # return copy
            
            # make new copy and update visited
            clonedNode = Node(node.val)
            visited[node] = clonedNode

            # go to neighbors of node and append to cloned node's neighbors
            for nei in node.neighbors:
                clonedNode.neighbors.append(dfs(nei))
            return clonedNode
        
        return dfs(node)
        
