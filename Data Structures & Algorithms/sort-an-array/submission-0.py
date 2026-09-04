class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        """
                10  9   1   1   1   2   3   1

        10  9   1   1                   1   2   3   1

    10 9            1   1           1   2           3   1
10        9       1        1       1      2       3        1
    9   10          1   1           1   2           1   3

        1   1   9   10                  1   1   2   3

                1   1   1   2   3   9   10


        mergeSort(arr, l, r)
            merge(arr, )
    
        """

        def merge(arr, L, M, R):
            left_subarr, right_subarr = arr[L:M+1], arr[M+1:R+1]
            arr_ptr, l_ptr, r_ptr = L, 0, 0

            while l_ptr < len(left_subarr) and r_ptr < len(right_subarr):
                if left_subarr[l_ptr] <= right_subarr[r_ptr]:
                    arr[arr_ptr] = left_subarr[l_ptr]
                    l_ptr += 1
                else:
                    arr[arr_ptr] = right_subarr[r_ptr]
                    r_ptr += 1
                arr_ptr += 1
            
            
            while l_ptr < len(left_subarr):
                nums[arr_ptr] = left_subarr[l_ptr]
                l_ptr += 1
                arr_ptr += 1

            while r_ptr < len(right_subarr):
                nums[arr_ptr] = right_subarr[r_ptr]
                r_ptr += 1
                arr_ptr += 1


        def mergeSort(arr, l, r):
            if l == r:
                return arr
            
            middle = (l + r) // 2

            mergeSort(arr, l, middle)
            mergeSort(arr, middle + 1, r)
            merge(arr, l, middle, r)

            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)