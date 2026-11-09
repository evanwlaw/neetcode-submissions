class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        we want to get the largest insignificant number and swap it to the most significant place -> start from right side to left


        """
        num = list(str(num))
        
        largestNum = "0"
        largestIdx = -1

        swapI, swapJ = 0, 0

        for i in range(len(num) - 1, -1, -1):
            if num[i] > largestNum: # find largest
                largestNum = num[i]
                largestIdx = i

            # swap
            if num[i] < largestNum:
                swapI = i
                swapJ = largestIdx

        num[swapI], num[swapJ] = num[swapJ], num[swapI]
        return int("".join(num))