class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Use sliding window

        window = [0] * 26


        z x y z x y z
            l
                r

        while window_freq[ord(s[r]) - ord('a')] > 1:
            window_freq[l] -= 1
            l += 1
        window_freq[ord(s[r]) - ord('a')] += 1
        ans = max(ans, r - l + 1)
        """

        window_freq = [0] * 95
        ans, l = 0, 0
        for r in range(len(s)):
            window_freq[ord(s[r]) - ord('a')] += 1

            while window_freq[ord(s[r]) - ord('a')] > 1:
                window_freq[ord(s[l]) - ord('a')] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
