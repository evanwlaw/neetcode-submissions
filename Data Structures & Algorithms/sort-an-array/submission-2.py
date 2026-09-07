class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        
        Input: nums = [10,9,1,1,1,2,3,1]
        Output: [1,1,1,1,2,3,9,10]

                                10,9,1,1,1,2,3,1
                    10,9,1,1                        1,2,3,1
            10, 9           1,1                 1,2         3, 1
        10          9      1    1              1    2      3     1
        merge
            9,  10          1,  1               1,  2       1,  3
                1,1,9,10                            1,1,2,3
                    1,1,1,1,2,3,9,10

        basecase: l_ptr == r_ptr -> return arr
        
        merge -> use 2 ptrs at the start of the two subarrays. put the smaller at nums[i]
        if left_sub[l_ptr] < right_sub[r_ptr]
            nums[i] = left_sub[l_ptr]
            l_ptr += 1
        else:
            nums[i] = right_sub[r_ptr]
            r_ptr += 1
        
        i += 1

        Time Complexity: O(NlogN) - O(logN) height of tree for the splits, at each level we need to process N elements -> Time complexity is O(NlogN)
        Space Complexity: O(N) - Need to have subarrays that hold all the values in input nums. We do sort nums in place by inserting from subarrays. So space complexity is based off of the O(N) needed for the subarrays in the mergesort
        """

        def merge(arr, l, middle, r):
            left_sub = arr[l:middle+1]
            right_sub = arr[middle+1:r+1]
            i, l_ptr, r_ptr = l, 0, 0

            while l_ptr < len(left_sub) and r_ptr < len(right_sub):
                if left_sub[l_ptr] < right_sub[r_ptr]:
                    arr[i] = left_sub[l_ptr]
                    l_ptr += 1
                else:
                    arr[i] = right_sub[r_ptr]
                    r_ptr += 1
                i += 1
            
            while l_ptr < len(left_sub):
                arr[i] = left_sub[l_ptr]
                l_ptr += 1
                i += 1
            while r_ptr < len(right_sub):
                arr[i] = right_sub[r_ptr]
                r_ptr += 1
                i += 1
            
        # recursive
        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            middle = (l + r) // 2
            # left
            mergeSort(arr, l, middle)

            # right
            mergeSort(arr, middle + 1, r)

            # merge both sides
            merge(arr, l, middle, r)

            return arr
        
        return mergeSort(nums, 0, len(nums))
