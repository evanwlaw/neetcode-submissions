class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        keep a window
        """

        hashMap = {}
        windowLen = 0
        l = 0

        for r in range(len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)

            while hashMap[s[r]] > 1:
                hashMap[s[l]] -= 1
                if hashMap[s[l]] == 0:
                    hashMap.pop(s[l])
                l += 1
            windowLen = max(windowLen, r - l + 1)
        return windowLen
