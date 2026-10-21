class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        use a hashmap that holds char : lastidx seen


        """

        hashMap = {} # char : last idx

        for i, c in enumerate(s):
            hashMap[c] = i
        
        output = []
        subStringLen = 0
        subStringIdx = 0

        for i, c in enumerate(s):
            subStringLen += 1
            subStringIdx = max(subStringIdx, hashMap[c])

            if subStringIdx == i:
                output.append(subStringLen)
                subStringLen = 0
        return output