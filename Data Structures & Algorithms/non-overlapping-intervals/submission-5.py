class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [1,2]   [2,4]   [1, 4]

        -------------
            ---------
        -----
        1   2   3   4

        idea: 
        to find nonoverlap, it's end of prev <= curr bgn
        overlap -> end of prev > curr gn
        
        """
        intervals.sort(key=lambda i:i[1])
        prevend = intervals[0][1]
        overlap = 0
        
        for i in range(1, len(intervals)):
            if prevend > intervals[i][0]:
                overlap += 1
            else:
                prevend = intervals[i][1]
            
        return overlap

