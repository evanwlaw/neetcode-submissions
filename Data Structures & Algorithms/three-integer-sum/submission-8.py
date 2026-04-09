class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        [-1,0,1,2,-1,-4]

        -4  -1  -1  0   1   2

        sort first.
        go through nums. at each [i], use two ptrs [i+1] and [len(nums) -1]. use 2sum

        
        """
        res = []
        nums.sort()
        r = len(nums) - 1
        for i, v in enumerate(nums):
            # skip the same number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                check_sum =  nums[i] + nums[l] + nums[r]

                if check_sum < 0: # move l
                    l += 1
                elif check_sum > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res



