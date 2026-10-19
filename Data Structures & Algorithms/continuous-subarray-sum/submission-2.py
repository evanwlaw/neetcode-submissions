class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        hashmap -> remainder : idx of where we saw it

        keep running sum mod k
        if we see remainder before, we means we found a number at some point that is a multiple of k that got added to the running sum
        """
        remainderMap = {0:-1} # remainder : idx seed with 0 with -1. we might first number as a multiple of k but that is a len of 1 not 2
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            r = total % k

            if r not in remainderMap:
                remainderMap[r] = i
            elif i - remainderMap[r] >= 2:
                return True

        return False
            