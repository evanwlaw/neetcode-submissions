from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Input: equations = [["a","b"],["b","c"],["ab","bc"]]
        values = [4.0,1.0,3.25]
        queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]
        Output: [4.00000,0.25000,1.00000,-1.00000,-1.00000]

        a/b * b/c = a/c  (cancel out b in numerator/denominator of terms)
        4   *  1  = 4

        Can think of terms like nodes (numerator points to denominator):
        a -> b -> c
        Edge weights are the values[i] in equations[i]
        a -> b : 4
        b -> c : 1
        
        So a -> c is 4
        However if there was a valid query for ["c", "a"], the answer would not be 4. It would be 1/4 (inverse).
        

        1. adjacency map of the equations.
        for each equation 
            build forward edge with given numerator/denominator with values[i]
            build back edge with inverse values[i]

        2. bfs function

        3. loop through queries (possibility of disconnected nodes/invalid):
            bfs search if queried nodes exist and get the return values
        
        4 return output list

        Time Complexity: O(Q * (N+E)) - Time is dominated by the bfs. Q is the num of queries and we may need to visit all nodes (N) and edges (E) in the bfs.
        Space Complexity: O(N+E) - We're using extra space to hold all the nodes and edges, so O(N+E) is used.

        '''
        adj_map = defaultdict(list) # numerator : [denominator, values[i]]

        # 1. adjacency map of the equations.
        for i, eq in enumerate(equations):
            num, den = eq # get numerator and denominator
            # forward edge
            adj_map[num].append([den, values[i]])
            # back edge
            adj_map[den].append([num, 1 / values[i]])

        # 2. bfs function
        def bfs(src: str, dest: str) -> float:
            # invalid, cannot be determined
            if src not in adj_map or dest not in adj_map:
                return -1

            queue = deque()
            queue.append([src, 1])
            visited = set()
            visited.add(src)

            while queue:
                node, weight = queue.popleft()
                if node == dest:
                    return weight

                for nei, nei_weight in adj_map[node]:
                    if nei not in visited:
                        queue.append([nei, nei_weight * weight])
                        visited.add(nei)
            return -1 # if we go through all neighbors and do not find st, then invalid
            
        # 3. loop through queries (possibility of disconnected nodes/invalid):
        output = []
        for q in queries:
            output.append(bfs(q[0],q[1]))
        # 4 return output list
        return output
