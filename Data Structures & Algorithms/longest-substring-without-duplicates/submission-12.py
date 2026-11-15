class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        windMap = {} # letter : freq

        for r in range(len(s)):
            windMap[s[r]] = 1 + windMap.get(s[r], 0)
            while windMap[s[r]] > 1:
                windMap[s[l]] -= 1
                if windMap[s[l]] == 0:
                    windMap.pop(s[l])
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen