class Solution:
    def maximumSwap(self, num: int) -> int:

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

