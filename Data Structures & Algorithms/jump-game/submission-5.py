class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Input: nums = [1,2,0,1,0]
        Output: true

        We need to keep track of jump lengths that get us from one idx to the other
        0   1   2   3   4
        1   2   0   1   0

        from nums[0] = 1:
            i += nums[0] = 1
        
        from nums[1] = 2
            i += nums[1] = 3
        
        from nums[3] = 1
            i += nums[3] = 4
        
        since i == 4 == len(nums) -> return True


        so we need to iterate through nums while i < len(nums) AND that nums[0] isnt 0
        if we terminate while loop, then return False

        Input: nums = [1,2,1,0,1]
        Output: false

        0   1   2   3   4
        1   2   1   0   1

        from nums[0] = 1
            i += nums[0] = 1
        
        from nums[1] = 2
            i += nums[1] = 3
        
        from nums[3] = 0
            i += nums[3] = 3

        we should update the while loop conditions be while i < len(nums) AND nums[i] != 0.
            if we encounter a 0, then we won't be able to reach the next position
        
        
        nums=[2,5,0,0]
        
        """
        # if len(nums) <= 1:
        #     return True
            
        # n = len(nums) - 1
        # i = 0
        # while i < n and nums[i] != 0:
        #     i += nums[i]
        #     if i >= n:
        #         return True
        # return False if i < n else True
        """
        Hellointerview solution

        track greedily how far we can go.
        max_reach is the further ith position we can go.
        
 
        """
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True