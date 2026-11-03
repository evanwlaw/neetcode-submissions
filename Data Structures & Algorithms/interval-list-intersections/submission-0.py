class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Input:
        firstList = [[0,2],[5,10],[13,23],[24,25]]
        secondList = [[1,5],[8,12],[15,24],[25,26]]

        Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

        0   1   2   3   4   5   6   7   8   9   10  11  12
        ---------           ----------------------
            -----------------           ------------------

        So basically, we want to return a list of places where there are overlaps

        overlap when
            1. firstList[end] >= secondlist[start]
                - in this case, move up firstList ptr
            2. firstList[start] >= secondList[end]
                - in this case, move up secondList ptr

        Time: O(m+n) where m is len of firstList and n is length of second list
        Space: O(N) for output list or just O(1) as we just use pointers

        """

        # fPtr = 0
        # sPtr = 0
        # output = []
        # while fPtr < len(firstList) and sPtr < len(secondList):
        #     if firstList[fPtr][1] >= secondList[sPtr][0]:
        #         output.append([max(firstList[fPtr][0], secondList[sPtr][0]), min(firstList[fPtr][1], secondList[sPtr][1])])
        #         fPtr += 1
        #     elif firstList[fPtr][0] >= secondList[sPtr][1]:
        #         output.append([max(firstList[fPtr][0], secondList[sPtr][0]), min(firstList[fPtr][1], secondList[sPtr][1])])
        #         sPtr += 1
        #     else:
        #         fPtr += 1
        #         sPtr += 1
        # return output
        """
        so i was on the right track, i just overcomplicated things.
        here's neetcode sol after reviewing
        """
        fPtr = 0
        sPtr = 0
        output = []

        while fPtr < len(firstList) and sPtr < len(secondList):
            startF, endF = firstList[fPtr]
            startS, endS = secondList[sPtr]

            start = max(startF, startS)
            end = min(endF, endS)

            if start <= end: # if in order, then intersection
                output.append([start,end])

            # update ptrs
            if endF < endS:
                fPtr += 1
            else:
                sPtr += 1
        return output
