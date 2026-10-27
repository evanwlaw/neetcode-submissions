from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        prereq[i] = [a,b] -> must take b before a
        b -> a indegree of b is 0

        return valid order (topological sort) in list otherwise empty if not possible

        1. build adj list and indegrees list
            - hashmap adjList {courseA:[neighbor courses that must take courseA ]}
                [b : a]
            - indegrees len(numCourses) -> indegrees[a] += 1 (edge from b to a)

        2. put course with 0 indegrees into queue (b will be in q) and in output
        3. for each neighbor/course in adjList[b]:
                indegree[a] -= 1
                ..
                ..
         
                if indegree[a] == 0 -> put into queue and put into output
        4. return output if len == numCourses else [] invalid
        """
        # [a,b]
        # 1. adjlist & indgrees
        adjList = defaultdict(list) # b : a
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            adjList[b].append(a)
            indegrees[a] += 1

        # 2. put 0 indegree courses into queue and in output
        output = []
        queue = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            output.append(course)
            
            for nei in adjList[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return output if len(output) == numCourses else []
        