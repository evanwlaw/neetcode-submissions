class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1   2   4
        ----
            ----
        --------

        Remove min number of overlaps -> sort by end of interval
        --------
            ----
        ----

        need to keep track of valid prev intervals.

        if intervals[i][0] < prev_start
        """

        if len(intervals) <= 1:
            return 0
        # sort by end
        intervals.sort(key=lambda x : x[1])
        prev_start = intervals[0][1]
        output = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_start:
                output += 1
            else:
                prev_start = intervals[i][1]
        return output

