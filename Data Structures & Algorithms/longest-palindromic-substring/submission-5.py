class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def findPal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        output = ""
        for i in range(len(s)):
            odd = findPal(i, i)
            even = findPal(i, i+1)
            if len(odd) > len(output):
                output = odd
            if len(even) > len(output):
                output = even
        return output