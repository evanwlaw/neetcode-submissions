class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        two ptrs
        use function to check if range is true or not 
        """
        # l, r = 0, len(s) - 1
        # def findPalindrome(s, l, r):
        #     start, end = l, r
        #     while l <= r:
        #         if s[l] != s[r]:
        #             return ""
        #         l += 1
        #         r -= 1
        #     return s[start:end + 1]


        # while l <= r:
        #     check = findPalindrome(s, l, r) or findPalindrome(s, l + 1, r) or findPalindrome(s, l, r - 1)
        #     if check:
        #         return check
        #     l += 1
        #     r -= 1
        """
        reviewed Neetcode solution
        """
        if len(s) <= 1:
            return s

        def findPal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        output = ""
        
        for i in range(len(s) - 1):
            odd = findPal(i, i)
            even = findPal(i, i + 1)
            if len(odd) > len(output):
                output = odd
            if len(even) > len(output):
                output = even
        return output