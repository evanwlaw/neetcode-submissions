class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        1. turn s into hashmap of char : # of times it's in the string

        2. go through order -> if order[i] in hashmap -> output.append(order[i] * hashMap[order[i]]) -> pop letter from hashmap
        3. append the rest hashmap if there is anything still left
        """

        sMap = {}

        for c in s:
            if c not in sMap:
                sMap[c] = 1
            else:
                sMap[c] += 1
        
        output = []
        for c in order:
            if c in sMap:
                output.append(c * sMap[c])
                sMap.pop(c)
        
        for c, v in sMap.items():
            output.append(c * v)
        return "".join(output)