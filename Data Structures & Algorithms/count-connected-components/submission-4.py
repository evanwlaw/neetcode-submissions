class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        ranking = [1] * n
        
        def find(n1):
            res = n1
            
            while res != parent[res]:
                # pull up
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
            
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
        for n1, n2 in edges:
            output -= union(n1,n2)
        return output