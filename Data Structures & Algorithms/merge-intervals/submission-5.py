class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Input: list of intervals (no guarantee that we're given an already sorted list)
        Output: return list with merged intervals where overlap occurs

        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
        —----
        —--------
                            —------
                            —------------
        Idea:
        Sort by start of each interval. Iterate through list from second interval in array and find overlap and merge. 

        Sort entire input by interval's start
        Put the first interval into output array.
        Iterate through intput array from second interval.
        Check if there overlap. Overlap is when the current interval's start <= previous interval's end (intervals[i][0] <= output[-1][1]). 
        Then merge the current interval with the last interval in the output
        output[-1][1] = max(output[-1][1], intervals[i][1])
            If no overlap, just append to output array.
        return output array

        Time Complexity: O(n logn) - Sorting will take O(nlogn) time. Iterating through a list is O(n). The sort dominates the time complexity, so O(n log n).
        Space Complexity: O(n) - If there are no overlaps, then we basically append all intervals into the output array, O(n). If there are overlaps then the array would be smaller than n elements - space complexity would be O(n) at most.
        Time to solve problem: 35 minutes
        '''

        intervals.sort(key=lambda interval: interval[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output
