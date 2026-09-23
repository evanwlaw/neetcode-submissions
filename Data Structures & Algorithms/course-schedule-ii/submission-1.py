class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        output = order of courses
        prereq [1,0] -> 1 is the course. 0 is the prereq

        so looks like we need to find topological sort order

        Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        Output: [0,2,1,3]

        1. adj map to get neighbors
        i   0   1   2   3
            1,2 2   3

        2. num of indegrees 
        i   0   1   2   3
                1   1   2

        from here, we enque courses that have no prereq/indegrees

        then iterate through queue:
            if 


        """

        adj_list = [[] for _ in range(numCourses)]
        indegrees = [0] * numCourses

        for c, p in prerequisites:
            adj_list[p].append(c)
            indegrees[c] += 1
        
        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        if not queue:
            return []
        
        output = []
        while queue:
            course = queue.popleft()

            for nei in adj_list[course]:
                indegrees[nei] -= 1

                if indegrees[nei] == 0:
                    queue.append(nei)

            output.append(course)
        if len(output) != numCourses:
            return []
        return output