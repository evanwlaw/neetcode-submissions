from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [0, 1] -> need to take 0 before course 1

        kahn's
        Input: numCourses = 2, prerequisites = [[1,0]]

        1. build indegrees numCourses and adjacency list
        indegrees list = 1, 0 -> need to take course 1 before 0. course 1 can be taken without anything else.

        each prereq is an edge from a_i <- b_i

        adj_list = {course a: prereqs}

        2. push to queue for each course with indegree of 0

        3. bfs through queue
        """

        indegrees = [0] * numCourses
        adj_list = defaultdict(list)
        for a, b in prerequisites:
            indegrees[a] += 1
            adj_list[b].append(a)
        
        queue = deque()
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)
        
        courses_processed = 0
        while queue:
            c = queue.popleft()
            courses_processed += 1

            for nei in adj_list[c]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)

        return courses_processed == numCourses
