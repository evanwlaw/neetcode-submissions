class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        union find.

        1. def find

        2. 
        """
        parent = [i for i in range(n)]
        ranking = [1] * n


        def find(n1):
            res = n1
            while res != parent[res]:
                # shift things upwards
                parent[res] = parent[parent[res]]
                res = parent[res]
            return res
        
        def union(n1, n2):
            n1p = find(n1)
            n2p = find(n2)

            if n1p == n2p:
                return 0
            # merge
            if ranking[n1p] < ranking[n2p]:
                parent[n1p] = n2p
                ranking[n2p] += ranking[n1p] 
            else:
                parent[n2p] = n1p
                ranking[n1p] += ranking[n2p] 
            return 1
        
        output = n
        for n1, n2 in edges:
            output -= union(n1, n2)
        return output

            