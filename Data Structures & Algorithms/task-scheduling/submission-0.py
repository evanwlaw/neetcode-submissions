class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        A: 3
        B: 3
        A B _ A B _ A B

        Input: tasks = ["A","A","A","B","C"], n = 3
        Output: 9
        A:3 , B:1, C:1
        A B C _ A _ _ _ A

        Have to process most frequent letter to minimize idle time.

        Use maxHeap of the letter/tasks counts.
        While maxHeap has items, pop it and put into queue until n time is up.

        Time Complexity: O(M log26) - M is the number of tasks where we have to iterate through all the M tasks until all counts are 0. Each iteration has push/pop ops that take up to O(log26) time.
        Space Complexity: O(26) - Space is used for the heap and queue which both combine would hold up to 26 letter pairs of counts:time.
        Time Spent on Problem: 30 minutes
        """
    
        # get letter counts in map and put into heap

        freq = Counter(tasks) # letter : count
        maxHeap = [-c for c in freq.values()]
        heapq.heapify(maxHeap)

        queue = deque() # [count, time]
        time = 0

        while maxHeap or queue:
            time += 1
            # if maxheap is empty, then move time to next in queue
            # this means we have to idle until then
            if not maxHeap:
                time = queue[0][1]
            else:
            # process from maxHeap
                count = heapq.heappop(maxHeap) + 1 # "decrease" the count
                if count:
                    queue.append([count, time + n]) # time + n is cooldown

            if queue and time == queue[0][1]:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
