class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        prerequisites -> [a,b] means a <- b where need to take b first before a

        Input: numCourses = 2, prerequisites = [[0,1]]
        Output: true

        we take course 1 first before 0. since 1 has no indegree, it can be taken first.

        kahns algorithm.
        1. setup adj_list and indegree list
        2. put courses with 0 indegrees into queue
        3. go through queue 
            - process courses and neighbors (decrement indegrees of neighbors and enqueue ones that have 0)
        4. True if processed courses matches numCourses


        """
        adj_list = defaultdict(list) # course : neighbors
        indegrees = [0] * numCourses # idx -> course and element -> # of indegrees

        for a, b in prerequisites:
            indegrees[a] += 1
            adj_list[b].append(a)
        
        queue = deque()
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
            
        processed = 0

        while queue:
            course = queue.popleft()
            processed += 1

            for nei in adj_list[course]:
                indegrees[nei] -= 1

                if indegrees[nei] == 0:
                    queue.append(nei)
                    




        return processed == numCourses
