class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i, n = 0, len(intervals)
        # step 1: append to res non overlap before netInt
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        # Step 2: merge newInterval with any overlap
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # add newInterval to res
        res.append(newInterval)

        # add any non overlap still left
        for i in range(i, n):
            res.append(intervals[i])
        return res