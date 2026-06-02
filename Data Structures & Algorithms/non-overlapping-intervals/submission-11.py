class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        sort by end
        find places of overlap and 'remove it'
        need to keep last valid interval

        """
        intervals.sort(key=lambda intervals:intervals[1])
        prev_valid = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_valid:
                res += 1
        
            else:
                prev_valid = intervals[i][1]
        return res