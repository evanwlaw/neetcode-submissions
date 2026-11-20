class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sCounts = {}
        for c in s:
            sCounts[c] = 1 + sCounts.get(c, 0)
        
        output = [] # if we use string, every append would be O(n) for each c (O(n^2) complexity for entire algo), so let's use array and return a join for O(n) time
        for c in order:
            if c in sCounts:
                output.append(sCounts[c] * c)
                sCounts.pop(c)
        for key, values in sCounts.items():
            output.append(key * values)

        return "".join(output)