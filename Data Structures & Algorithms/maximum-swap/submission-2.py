class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        move most largest insignificant digit with the smallest most significant

        1. turn int into str list
        2. increment backwards
            find largest num and it's idx:  
            if nums[i] > maxVal -> update maxVal and maxIdx to nums[i] and i
            if nums[i] < maxVal -> this is candidate to swap with maxVal

        9   8   3   6   8
            i
        maxVal = "0"
        maxIdx = -1
        
        1st iter:
        maxVal = "8"
        maxIdx = 4
        

        2nd iter:
        maxVal = "8"
        maxIdx = 4
        nums[i] 6 -> candidate to swap with 8
        swapMaxI = maxIdx
        swapCand = i = 3

        3rd iter:
        maxVal = "8"
        maxIdx = 4
        nums[i] = 3 -> better candidate to swap with 8
        swapMaxI = maxIdx
        swapCand = i = 2

        4th iter
        maxVal = "8"
        maxIdx = 4
        nums[i] = 8 -> same as maxval.
        no need to update

        5th iter
        same result as previous

        swap nums[swapMaxI] with nums[swapCand] -> 8 and 3 swap
        return int("".join(num)) -> 98863
        Time: O(N)
        Space: O(N)
        """
        if num < 10:
            return num

        maxVal = "0"
        maxIdx = -1
        swapMaxI, swapCand = -1, -1
        num = list(str(num))

        for i in range(len(num)-1, -1, -1):
            if num[i] > maxVal: # find and update max value seen
                maxVal = num[i]
                maxIdx = i
            # find the candidate number to swap
            if num[i] < maxVal:
                swapCand = i
                swapMaxI = maxIdx
        # swap
        num[swapCand], num[swapMaxI] = num[swapMaxI], num[swapCand]

        return int("".join(num))

