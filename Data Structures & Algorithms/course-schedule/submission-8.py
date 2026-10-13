from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        prerequisites -> [a,b] -> need to take b first before a

        b -> a
        topological sort -> kahn's

        need to get indegrees and adjMap -> course : neigbors
        """

        indegrees = [0] * numCourses
        adjMap = defaultdict(list) # course : neighbors

        # 1. update adjmap and indegrees
        for a,b in prerequisites:
            adjMap[b].append(a)
            indegrees[a] += 1
        
        # enqueue courses without prereqs
        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        # bfs
        processedCourses = 0
        while queue:
            course = queue.popleft()
            processedCourses += 1

            for nei in adjMap[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return processedCourses == numCourses
