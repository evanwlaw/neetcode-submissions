class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A): # put longer list as A aka left partition
            A, B = B, A
        
        l, r = 0, len(A) - 1 

        while True:
            i = l + (r - l) // 2 # mid of A
            j = half - i - 2 # get same pos of mid as A's mid. both i and j starts at 0.
            
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i+1] if i+1 < len(A) else float("inf")         

            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")


            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # aleft is too big. too many elements in A
                r = i - 1 # reduce size of A
            else:
                l = i + 1