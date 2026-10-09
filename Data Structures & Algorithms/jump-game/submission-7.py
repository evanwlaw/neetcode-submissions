class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Input: nums = [1,2,0,1,0]
        Output: true
        0   1   2   3   4
        1   2   0   1   0

        if nums[0] == 0, then return False immediately as we cant get anywhere
        So the nums[i] -> furtherest that we can go. e.g. if 2, we can go 1 or 2 jumps. nums[1] can get use to nums[2] or nums[3] -> in this case we want to go nums[3]

        Input: nums = [1,2,1,0,1]
        Output: false
        0   1   2   3   4
        1   2   1   0   1

        
        we want to greedily track how far we can reach with all the nums[i] we've seen for. 
        in second ex, nums[1] and nums[2] gets us furthest to nums[3].
        even inclusion of nums[3], will not get us anywhere. as we iterate through nums, if we see that our ith iteration passed the maxReach of all jumps, then we know we couldnt reach the last position

        """
        
        maxReach = 0
        
        for i in range(len(nums)):
            if maxReach < i:
                return False
            maxReach = max(maxReach, i + nums[i])

        return True