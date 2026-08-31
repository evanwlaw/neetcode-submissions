class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Input: intervals = [[1,3],[1,5],[6,7]]
        Output: [[1,5],[6,7]]

        1   2   3   4   5   6   7
        ---------
        -----------------
                            -----


        Input: intervals = [[1,2],[2,3]]
        Output: [[1,3]]

        1   2   3
        -----
            -----


        No guarantee that intervals is sorted. If we iterate through it, we won't be able to see if curr interval has overlap with previous unless we sort intervals by start.

        Once sorted by start,
            if current interval start <= previous interval end -> found overlap
                merge by finding which one has a larger end intervals (sorted by start already)
                append to output
            else -> it's not overlapping
                append to output
        Time Complexity: O(N log N) - sort algo takes O(NlogN). Loop is O(N) with O(1) ops per iteration. 
        Space Complexity: O(1) - sorted in place. and no extra space is used.
        Time spent: <20 minutes
        """
        if len(intervals) <= 1:
            return intervals

        intervals.sort()

        output = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output
