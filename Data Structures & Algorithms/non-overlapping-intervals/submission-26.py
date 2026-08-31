class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        output = 0
        # sort by end of intervals
        intervals.sort(key=lambda x: x[1])
        prevValid = intervals[0]		
        
        for i in range(1, len(intervals)):
            # overlap found. increment output, keep prevValid and do not record overlap
            if intervals[i][0] < prevValid[1]:
                output += 1
            else:
                prevValid = intervals[i]
        return output
