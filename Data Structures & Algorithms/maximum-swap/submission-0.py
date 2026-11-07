class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        turn num into str
        """
        num = list(str(num))
        
        maxDigit = "0"
        maxI = -1

        swapI, swapJ = -1, -1

        for i in range(len(num) - 1, -1, -1):
            # get max
            if num[i] > maxDigit:
                maxDigit = num[i]
                maxI = i
            
            # swap
            if num[i] < maxDigit:
                swapI, swapJ = i, maxI
            
        num[swapI], num[swapJ] = num[swapJ], num[swapI]
        return int("".join(num))