class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        
        """
        
        window = 0
        max_sum = nums[0]

        for n in nums:
            window = max(n, window + n)
            max_sum = max(window, max_sum)
        return max_sum
            
