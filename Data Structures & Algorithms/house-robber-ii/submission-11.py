class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.findMax(nums[:-1]), self.findMax(nums[1:]))
    
    def findMax(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        prev2, prev1 = 0, 0
        for i in range(n):
            temp = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = temp
        return prev1

        