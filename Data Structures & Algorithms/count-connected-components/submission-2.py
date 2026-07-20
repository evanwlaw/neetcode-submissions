class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        node : neighbors
        0 : 1
        1 : 0, 2
        2 : 1

        3 : 4
        4 : 3
        

        1 : 2, 3
        2 : 1, 3
        3 : 1, 2
        '''
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0] * n
        
        def dfs(node):
            if visited[node] != 0:
                return
            
            visited[node] = 1
            
            for nei in adj[node]:
                dfs(nei)
            return


        output = 0
        for node in range(n):
            if visited[node] == 0:
                dfs(node)
                output += 1
        return output
