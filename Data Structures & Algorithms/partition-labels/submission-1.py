class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        a char cant appear in more than on substring...

        we need to track the last idx of a char appearing in the string

        use a map -> char : lastidx

        iterate through s
            increment sustring len +1
            end of substring = max(currend, map[c])

            if i == end of string:
                output.append(substring len)
        """

        lastInd = {} # char : lastIdx

        for i, c in enumerate(s):
            lastInd[c] = i

        output = []
        substringLen = 0
        substringEnd = 0
        for i, c in enumerate(s):
            substringLen += 1
            substringEnd = max(substringEnd, lastInd[c])

            if substringEnd == i:
                output.append(substringLen)
                substringLen = 0
        return output 