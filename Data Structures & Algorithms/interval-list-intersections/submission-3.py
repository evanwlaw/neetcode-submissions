class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fPtr, sPtr = 0, 0
        output = []

        while fPtr < len(firstList) and sPtr < len(secondList):
            fStart, fEnd = firstList[fPtr]
            sStart, sEnd = secondList[sPtr]

            start = max(fStart, sStart)
            end = min(fEnd, sEnd)

            if start <= end: # intersection
                output.append([start, end])
            
            # update ptr. move the one that has an earlier end
            if fEnd < sEnd:
                fPtr += 1
            else:
                sPtr += 1
        return output