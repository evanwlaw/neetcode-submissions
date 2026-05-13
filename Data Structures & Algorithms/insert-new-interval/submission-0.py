class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        [1,3] [4,6] [6,7] [8,10] [11,15]
        [5,8]

        [1,3] [4,10] [11,15]

        1. append ones before the overlap/newinterval
        when intervals[i][1] < newInterval[0]

        2. merge overlaps
        when intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])

        3. append overlap
        res.append(newInterval)

        4. append the rest of the intervals
        """
        res = []
        i, n = 0, len(intervals)


        # 1. append ones before the overlap/newinterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. merge overlaps
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        # 3. append overlap
        res.append(newInterval)

        # 4. append the rest of the intervals
        for i in range(i, n):
            res.append(intervals[i])
        
        return res
