class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Input: nums = [2,9,8,3,6]
        Output: 16
        Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.


        dp(5) = max(dp(4), dp(3) + nums[i])
        dp(i) = max(dp(i - 1), dp(i-2) + nums[i])
        '''
        
        prev1, prev2 = 0,0
        

        for n in nums:
            temp = max(n + prev1, prev2)
            prev1 = prev2
            prev2 = temp
        return prev2