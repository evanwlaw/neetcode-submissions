class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        turn nums into set

        for i in range(len(nums):
            if nums[i] - 1 not set: # this means we're at the beginning
                while nums[i] + 1 in set:
                    res += 1
                


        """

        set(nums)
        res = 0
        for n in nums:
            if n - 1 not in nums:
                length = 1
                while n + length in nums:
                    length += 1
                res = max(res, length)
        return res


