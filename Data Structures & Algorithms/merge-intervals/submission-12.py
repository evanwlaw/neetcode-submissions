class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        we want to sort by start times

        1   2   3   4   5   6   7
        ---------
        -----------------
                            ------
        """
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x:x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if output[-1][1] >= intervals[i][0]:
                output[-1][0] = min(output[-1][0], intervals[i][0])
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output

        