class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window hashmap
        """
        seen = set()
        output = 0
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            output = max(output, (r - l + 1))
        return output


