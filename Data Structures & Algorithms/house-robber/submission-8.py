class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Input: nums = [2,9,8,3,6]
        Output: 16 -> nums[0] + nums[2] + nums[4]

        at each house -> rob or don't rob

        at nums[0] -> 2
            - take or dont take?
                take because we dont have anything
            - what we know:
                - rob nums[0] as it gives max money
                - curr max: 2
        
        at nums[1] -> 9
            - take or dont take?
                take because it's larger than robbing nums[0]
            - what we know:
                - rob nums[1] as it gives max money
                - curr max: 9
        
        at nums[2] -> 8
            - take or dont take?
                take -> nums[0] + nums[2] > nums[1] (10 > 9)
            - what we know:
                - rob nums[2] as it gives max money
                - curr max: 10
        
        at nums[3] -> 3
            - take or dont take?
                take -> nums[0] + nums[2] < nums[1] + nums[3] (10 < 12)
            - what we know:
                - rob nums[3] as it gives max money
                - curr max: 12
        
        at nums[4] -> 6
            - take or dont take?
                take -> nums[0] + nums[2] + nums[4] > nums[1] + nums[3] (16 > 12)
            - what we know:
                - rob nums[4] as it gives max money
                - curr max: 16
        
        Seems it is dp. At each house, we recompute the previous houses that we robbed and see if the current one + the houses combined i-2.

        For example, at house 
            house i = 2 -> max is 9 (nums[1] is largest)
            house i = 3 -> max is 10 (nums[2] is largest). 

        Each house, we need to figure out if dp[i-1] is larger than dp[i-2] + curr house money
        So dp[i] is the max total money up to the ith + 1 house. 
        
        base case:
        dp[0] = 0
        dp[1] = nums[0]
        
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-1] ,dp[i-2] + nums[i-1])
        return dp[len(nums)]
