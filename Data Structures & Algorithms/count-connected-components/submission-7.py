from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        iterate through nodes
            dfs
            component += 1

        return component

        """

        # create adj list
        adj_list = defaultdict(list) # node : neighbor
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in adj_list[node]:
                dfs(nei)
            return                
        
        component = 0
        # iterate through nodes
        for i in range(n):
            if i not in visited:
                dfs(i)
                component += 1
        return component