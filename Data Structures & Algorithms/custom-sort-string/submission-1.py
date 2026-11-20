class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Input: order = "xabfcg", s = "bdca"
        Output: "abcd"

        hashmap with s's char : occurences

        iterate through order:
            if order[i] in hashmap:
                output += hashmap[order[i]] * order[i]
        """

        sCounts = {}
        for c in s:
            sCounts[c] = 1 + sCounts.get(c, 0)
        # print(sCounts.items())
        
        output = [] # if we use string, every append would be O(n) for each c (O(n^2) complexity for entire algo), so let's use array and return a join for O(n) time
        for c in order:
            if c in sCounts:
                output.append(sCounts[c] * c)
                sCounts.pop(c)
        print(output)
        for key, values in sCounts.items():
            output.append(key * values)

        return "".join(output)