class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Input: nums = [2,20,4,10,3,4,5]
        Output: 4

        iterate through nums
            nums[0] ->  2
            we know the current num at ith place.
            we dont know if this is start of a consecutive sequence or not (it is for the answer but need a variable to tell).
            we dont know if contributes to the longest consecutive sequence.
            
            nums[1] ->  20
            we know the current num at ith place.
            we dont know if this is start of a consecutive sequence or not.
            we dont know if contributes to the longest consecutive sequence.

            nums[2] ->  4
            we know the current num at ith place.
            we dont know if this is start of a consecutive sequence or not.
            we dont know if contributes to the longest consecutive sequence.

        nums[0] = 2 is the start of the sequence because nums[0] - 1 doesnt exist in nums

        duplicates should not count towards output len.

        1. run through nums and put all into the set
        2. iterate through nums. 
            if it's a start of a sequence,
                keep incrementing as long as the next value is in the set
        Time complexity: O(N) - Creating the set is O(N) time. In the for loop, we only go into the while loop if it's the start of a sequence, we won't go into it if we've seen it before on another sequence. Worst case is O(N).
        Space complexity: O(N) - Extra space is used to hold all the unique ints from the input nums. Worst case is each one is unique, so up to O(N) space is used.
        Time spent on problem: 25 minutes
        """

        nums_set = set(nums)
        output = 0

        for n in nums:
            if n - 1 not in nums_set:
                curr_len = 1
                while n + 1 in nums_set:
                    curr_len += 1
                    n += 1
                output = max(curr_len, output)
        return output
                