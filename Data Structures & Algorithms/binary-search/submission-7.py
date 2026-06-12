class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            
            if nums[middle] < target:
                l = middle + 1
            elif nums[middle] > target:
                r = middle - 1
            else:
                return middle
        return -1
