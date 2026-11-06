class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        0   1   2   3   4   5   6   7   8   9   10  11  12  13
        ---------           ----------------------           ----
            -----------------           -------------------
        """
        fPtr, sPtr = 0, 0
        output = []
        while fPtr < len(firstList) and sPtr < len(secondList):
            fStart, fEnd = firstList[fPtr]
            sStart, sEnd = secondList[sPtr]
            
            # interection when 
            if fEnd >= sStart and fStart <= sEnd:
                output.append([max(fStart,sStart), min(fEnd, sEnd)])

            if fEnd < sEnd:
                fPtr += 1
            else:
                sPtr += 1
        return output

