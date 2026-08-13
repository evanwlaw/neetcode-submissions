class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        AAABABB
        ------
        A:4
        B:2

        We know the max values of letter. need to find the smallest number. 

        Use hashmap to track freq

        smallest freq of letter in window= len(window) - max(most freq letter)

        while smallest freq letter in window is > k:
            pop from left

        """
        freq = {}
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            while r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res




