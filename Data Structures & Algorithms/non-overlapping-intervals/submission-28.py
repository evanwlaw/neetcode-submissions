class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        return how many intervals needed to remove for non overlap

        1   2   3   4   5
        -----
        --------------
            ----------

        """
        if not intervals or len(intervals) <= 1:
            return 0
        
        intervals.sort(key= lambda x :x[1] )
        validInt = intervals[0]
        output = 0
        print(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] < validInt[1]:
                output += 1
            else:
                validInt = intervals[i]

        return output