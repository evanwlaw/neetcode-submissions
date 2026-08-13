class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1   2   4
        ---- 
            -----
        ---------
        Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
        Output: 1
        Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

        1   2   3   4
        ---
            ---
        -------
                ----


        intervals=[[1,100],[11,22],[1,11],[2,12]]

         1,11
         2,12
        11,22
        1,100

        sort by last interval

        if intervals[i][0] < intervals[i - 1][0] 
            res += 1
        """
        intervals.sort(key=lambda x: x[1])
        prev = [intervals[0][0], intervals[0][1]]
        output = 0

        for i in range(1, len(intervals)):
            
            if intervals[i][0] < prev[1]:
                output += 1
            else:
                prev = [intervals[i][0], intervals[i][1]]
        return output