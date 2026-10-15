class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        two passes
        first pass to get the index of where it last showed -> put in map
        second to get how long
        """

        lastIndex = {} # char : last idx
        res = []
        for i, c in enumerate(s):
            lastIndex[c] = i
        
        substringLen = 0
        substringEnd = 0
        for i, c in enumerate(s):
            substringLen += 1
            substringEnd = max(substringEnd, lastIndex[c])
            if substringEnd <= i:
                res.append(substringLen)
                substringLen = 0
        return res