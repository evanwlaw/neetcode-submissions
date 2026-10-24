class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        check valid palindrom.

        two ptrs
        """

        def check(s, l, r):            
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l,r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return check(s, l + 1, r) or check(s, l, r - 1)
            l += 1
            r -= 1
        return True