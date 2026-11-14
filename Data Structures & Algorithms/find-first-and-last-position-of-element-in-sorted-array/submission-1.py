class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        binary search [left, right]
        """
        def binarySearch(leftStart):
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                middle = l + (r-l) // 2

                if target > nums[middle]:
                    l = middle + 1
                elif target < nums[middle]:
                    r = middle - 1
                else: # match, now find the furthest one
                    idx = middle

                    if leftStart:
                        r = middle - 1
                    else:
                        l = middle + 1
            return idx
        return [binarySearch(True), binarySearch(False)]
        
        