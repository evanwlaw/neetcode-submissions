class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        output = []

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        # 0 = unvisited
        # 1 = visiting
        # 2 = done processing
        state = [0] * numCourses

        def dfs(c):
            if state[c] == 1:   # cycle
                return False    

            if state[c] == 2: # safe as we checked no cycle
                return True

            state[c] = 1

            for neighbor in adj[c]:
                if not dfs(neighbor):
                    return False
            state[c] = 2
            output.append(c)
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output
