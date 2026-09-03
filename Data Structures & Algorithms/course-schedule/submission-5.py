class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        prerequisites a <- b - take b before can take a

        if a course as no prereq that means no indegrees -> we can take this course.


        Build adjlist with indegrees



        """

        adjList = defaultdict(list)
        indegrees = [0] * numCourses

        for a, b in prerequisites:
            adjList[b].append(a) # b -> a
            indegrees[a] += 1

        # find the ones without indegress and queue them up.
        queue = deque()

        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.append(course)

        visited = 0

        while queue:
            course = queue.popleft()

            visited += 1

            for nei in adjList[course]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        return True if visited == numCourses else False
