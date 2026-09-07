class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        [10,9,1,1,1,2,3,1]


        """

        def merge(arr, l, middle, r):
            left_sub = arr[l:middle]
            right_sub = arr[middle:r]

            i, l_ptr, r_ptr = l, 0, 0

            while l_ptr < len(left_sub) and r_ptr < len(right_sub):
                if left_sub[l_ptr] <= right_sub[r_ptr]:
                    arr[i] = left_sub[l_ptr]
                    l_ptr += 1
                else:
                    arr[i] = right_sub[r_ptr]
                    r_ptr += 1
                
                i += 1

            # one sub arr might be bigger than the other, just fill
            while l_ptr < len(left_sub):
                arr[i] = left_sub[l_ptr]
                i += 1
                l_ptr += 1

            while r_ptr < len(right_sub):
                arr[i] = right_sub[r_ptr]
                i += 1
                r_ptr += 1


        def mergeSort(arr, l, r):
            if r - l <= 1:
                return
            
            middle = (l + r) // 2
            mergeSort(arr, l, middle)
            mergeSort(arr, middle, r)

            merge(arr, l, middle, r)

        mergeSort(nums, 0, len(nums))
        return nums
