class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)

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
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
