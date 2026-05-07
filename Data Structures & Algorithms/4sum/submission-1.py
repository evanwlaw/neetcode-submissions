class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        backtracking ksum
        basecase is k = 2

        """
        nums.sort()
        res, quad = [], []

        def ksum(k, start_idx, target):
            if k == 2:
                l, r = start_idx, len(nums) - 1

                while l < r:
                    if nums[l] + nums[r] < target:
                        l +=1
                    elif nums[l] + nums[r] > target:
                        r -=1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                return
            
            # recurse through k
            for i in range(start_idx, len(nums) - k + 1):
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue
                
                quad.append(nums[i])
                ksum(k - 1, i + 1, target - nums[i])
                quad.pop()

        
        ksum(4, 0, target)
        return res