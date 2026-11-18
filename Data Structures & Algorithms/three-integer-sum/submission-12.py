class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort the array

        -4      -1      -1      0       1       2
                i
                        l
                                                r

        """
        if not nums or len(nums) < 3:
            return []
        nums.sort()
        output = []
    
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                checkSum = nums[i] + nums[l] + nums[r]
                if checkSum < 0:
                    l += 1
                elif checkSum > 0:
                    r -= 1
                else: # found target
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return output

