class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1   2   3   4
        -----
            -----
        -------------

        1   11  12   22  50  100
        -------
            ------
          --------
            -----------
        ------------------------

        sort by the end -> maximize the number of intervals.

        overlap when
        intervals[i][start] < intervals[i-1][end]
        """
        intervals.sort(key=lambda x:x[1])
        lastValid = intervals[0]
        output = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastValid[1]:
                output += 1
            else:
                lastValid = intervals[i]
        return output