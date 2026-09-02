class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        kahn's

        1. get indegrees

        2. queue up indegree of 0

        3. bfs. only queue up if/when indegree is 0

        """

        indegrees = [0] * numCourses
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
            indegrees[prereq] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        visited = 0 

        while queue:
            course = queue.popleft()
            visited += 1

            for nei in adjList[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return visited == numCourses