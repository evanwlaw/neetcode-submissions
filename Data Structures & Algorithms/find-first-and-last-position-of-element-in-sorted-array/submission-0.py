class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        binary search twice to find the left and the right one
        """
        left = self.binarySearch(target, nums, True)
        right = self.binarySearch(target, nums, False)
        
        return [left,right]


    def binarySearch(self, target, nums, findLeft):
        l, r = 0, len(nums) - 1
        idx = -1

        while l <= r:
            m = l + (r - l) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else: # found target at m
                idx = m    

                # if findLeft -> go towards left side to find smallest
                if findLeft:
                    r = m - 1
                else:
                    l = m + 1
        return idx