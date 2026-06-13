class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1   2   3   4   5   6   7   8   9   10
        ---------
                    ---------               
            -------------
        """
        res = []
        i, n = 0, len(intervals)
        # append nonoverlaps
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # merge overlaps
        while i < n and intervals[i][0] <= newInterval[1]:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
                i += 1
        
        res.append(newInterval)

        # append everything else
        for j in range(i, n):
            res.append(intervals[j])
        return res