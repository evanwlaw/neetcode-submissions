class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        6,6,7,7,8

        '''
        nums.sort()
        i, n = 0, len(nums)
        while i < n - 1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[i]