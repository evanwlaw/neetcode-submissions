class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        1   2   3   4   5   6   7
        ---------
        -----------------
                            -----
        if points are starting on same, they overlapping. [1,2] and [2,3] ->[1,3]

        input is not gurantted to be sorted.
        let's sort based on each intervals start

        1   2   3   4   5   6   7
        ---------
        -----------------
                    ---------
                            -----
        
        output is seeded with intervals[0]

        overlap if intervals[i][start] <= output[last][end]:
            merge:
                output[last][start] = min(output[last][start], intervals[i][start]) 
                output[last][end] = max(output[last][end], intervals[i][end])
        otherwise, we can just append intervals[i] 
        """

        intervals.sort(key=lambda x:x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][0] = min(output[-1][0], intervals[i][0]) 
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output

