class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        we need to see if we're able to get to the last indx of nums input.

        we can go at MOST nums[i]. 

        Input: nums = [1,2,0,1,0]
        Output: true
        
        nums[1] can go to nums[2] OR nums[3] bc of the 2

        we can track how far we can go current nums[i].
            if maxDist < i -> then we can't reach
        """


        maxDist = 0

        for i in range(len(nums)):
            if i > maxDist:
                return False
            maxDist = max(maxDist, i + nums[i])

        return True
            