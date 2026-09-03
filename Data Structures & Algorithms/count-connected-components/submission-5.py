class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        ranking = [1] * n

        def find(n1):
            curr = n1
            while curr != parent[curr]:
                # shift upwards
                parent[curr] = parent[parent[curr]]
                curr = parent[curr]
            return curr

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            if ranking[p1] > ranking[p2]:
                parent[p2] = p1
                ranking[p1] += ranking[p2]
            else:
                parent[p1] = p2
                ranking[p2] += ranking[p1]
            return 1
        
        output = n
        for ai, bi in edges:
            output -= union(ai, bi)
        return output