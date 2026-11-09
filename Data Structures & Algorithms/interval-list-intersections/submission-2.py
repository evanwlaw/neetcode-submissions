class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fPtr, sPtr = 0, 0
        output = []
        while fPtr < len(firstList) and sPtr < len(secondList):
            fStart, fEnd = firstList[fPtr] 
            sStart, sEnd = secondList[sPtr]

            start, end = max(fStart,sStart), min(fEnd, sEnd)

            if start <= end:
                output.append([start, end])

            if fEnd < sEnd:
                fPtr += 1
            else:
                sPtr += 1
        return output