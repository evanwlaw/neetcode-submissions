class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1   2   3   4   5
        -----
            ---------
        -------------

        You need to track the end of the last interval you decided to keep
        not just the previous interval in the array.
        """
        intervals.sort(key=lambda i: i[1])
        res = 0
        prev_valid_int = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_valid_int:
                res += 1
            else:
                prev_valid_int = intervals[i][1]
        return res

