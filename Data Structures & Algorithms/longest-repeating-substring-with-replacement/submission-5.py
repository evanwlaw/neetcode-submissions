class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """ 
        output is the longest len of str we can have by changing k char

        count {v:count}

        increment count when within k



        while num of replacements is > k,
            decrement count of s[l]
        """

        l, res = 0, 0
        count = {} # v:count

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, (r-l+1))
        return res
            
            