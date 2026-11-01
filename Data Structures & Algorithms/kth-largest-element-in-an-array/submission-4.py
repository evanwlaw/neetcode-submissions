import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        quick select recursive
        in place sort
        """
        k = len(nums) - k # the idx we're going to look for the ans

        def quickSelect(l, r):
            pivot, ptr = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[ptr], nums[i] = nums[i], nums[ptr]
                    ptr += 1
            # swap ptr with pivot
            nums[ptr], nums[r] = nums[r], nums[ptr]

            if ptr > k:
                return quickSelect(l, ptr - 1)
            elif ptr < k:
                return quickSelect(ptr + 1, r)
            else:
                return nums[ptr]
        return quickSelect(0, len(nums) - 1)