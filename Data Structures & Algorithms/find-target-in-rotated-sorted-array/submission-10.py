class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Input: sorted array that is rotated at a pivot.
        Output: return the idx of the target if found, otherwise -1 not found

        Idea:
        Use binary search. 


        4	5	6	7	0	1	2
                        T
        m
        l
                                r
            
        7 	0	1	2	4	5	6
                        T
                    m
        l
                                r

        initialize left as 0 and right as length of array -1.
        while left < right:
            Get middle -> left + (right - left) // 2
            if nums[middle] == target, return nums[middle]

        First find which half of the search space is the sorted portion.
            if nums[left] <= nums[middle] -> this means the left side (left:middle) is sorted portion.

                Find if target is on left or right side of array by seeing if target is in sorted portion first.
        If nums[left] <= target <= nums[middle] -> target is potentially on the left side. Move right ptr -> middle - 1.
        else target is potentially on right side. Move left ptr -> middle + 1.

            else right side is sorted portion where nums[middle] <= nums[right]
                Find if target is on left or right side of array.
        If nums[middle] <= target <= nums[right] -> target is potentially on the right side. Move left ptr -> middle + 1.
        else target is potentially on left side. Move right ptr -> middle - 1.

        if we're here past the while loop, then it means we didnt find target in the array

        Time Complexity: O(log n) - By going through the input in binary search fashion, we go through it in O(log n) time.
        Space Complexity: O(1) - We're only using pointers for extra space, so O(1).

        Time to solve problem: 40 min
        '''

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            
            if target == nums[middle]:
                return middle

            # First find which half of the search space is the sorted portion.
            if nums[left] <= nums[middle]: # left side is sorted portion
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle -1
        return -1 # if here, means didn't find target
