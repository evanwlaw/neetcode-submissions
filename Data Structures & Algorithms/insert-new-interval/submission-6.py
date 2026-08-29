class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        in intervals, merge newInterval if there are overlaps

        Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
        Output: [[1,6]]
        1   2   3   4   5   6
        ---------   --------- intervals
            -------------       newInterval


        1   2   3   4   5   6   7   8   9   10
        -----   ---------               ------ intervals
                            -----               newIntervals

        iterate through intervals
            we don't if current interval overlaps with newinterval
                - need to compare if overlap (overlap if intervals[i][1] > newInterval[0])
        Step 1: first append to output list the nonoverlapping -> if intervals[i][1] < newInterval[0]
        Step 2: merge overlaps and append.
            - intervals overlap if intervals[i][0] <= newIntervals[1] 
        Step 3: append the rest

        Time complexity: O(N) - iterate through the enitre intervals once + O(1) ops
        Space complexity: O(1) - output is given. and we only have pointers ot hold for extra space
        """

        output = []
        i, n = 0, len(intervals)

        # append nonoverlaps
        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1
        
        # merge overlaps
        while i < n and intervals[i][0] <= newInterval[1]:
            # extend overlap
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        # merge
        output.append(newInterval)

        # append what's left
        for j in range(i, n):
            output.append(intervals[j])
        return output