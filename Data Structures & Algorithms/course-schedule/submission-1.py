class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # adjList = { course: preq}
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        # 0 not processed, 1 visiting, 2 completed
        state = [0] * numCourses

        def dfs(course):
            # check if cycle
            if state[course] == 1:
                return False
            
            # if 2, then we processed and chcked for cycles. Safe
            if state[course] == 2:
                return True
            
            state[course] = 1

            for nei in adjList[course]:
                if not dfs(nei):
                    return False
            state[course] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
