class Solution:
    def jump(self, nums: List[int]) -> int:
        # if nums[0] == 0:
        #     return 0
        # numJumps = 1
        # maxReach = 0
    
        # for i in range(len(nums)):
            
        #     maxReach = max(maxReach, i + nums[i])
        #     numJumps += 1
        #     if maxReach <= len(nums):
                
        #         return numJumps

        """
        reviewed the neetcode solution.

        still uses greedy -> kinda of like bfs lvls where each "level" is the nums[l:r+1] we were able to jump to from nums[i]
        """
        res = 0
        l = r = 0

        while r < len(nums) - 1: # r is the further boundary
            furthestReach = 0

            # find the l and r of the next jump layer
            for i in range(l, r + 1):
                furthestReach = max(furthestReach, i + nums[i])
            # update pointers
            l = r + 1
            r = furthestReach
            # increment jumps
            res += 1
        return res
