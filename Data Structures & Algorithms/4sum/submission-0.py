class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        first sort nums

        -3  0   1   2   3   3
            l            


        """ 
        n = len(nums)
        res = []
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            for j in range(i + 1, n):
                if j > i+1 and nums[j] == nums[j-1]: continue
                l,r = j + 1, n - 1
                
                while l < r:
                    summ = nums[i] + nums[j] + nums[l] + nums[r]

                    if summ < target:
                        l += 1

                    elif summ > target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res
                        

                    

