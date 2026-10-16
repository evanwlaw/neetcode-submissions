class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        we need to find out the len of substrings. with each letter appearing at most in one of these substring.

        so we need to track the last idx of each char in string -> used hashmap

        
        then iterating through s:
            keep track of current substring len
                increment substring len
            keep track of current substring's last idx
                max(substringlastidx, last idx of s[i])

            if i == substringlen, then means substring is valid
                append substring len to output
                reset substringlen
        """

        lastIdxMap = {}

        for i, c in enumerate(s):
            lastIdxMap[c] = i
        
        substringLen = 0
        substringIdx = 0
        output = []
        for i, c in enumerate(s):
            substringLen += 1
            substringIdx = max(substringIdx, lastIdxMap[c])

            if substringIdx == i:
                output.append(substringLen)
                substringLen = 0
        return output
            