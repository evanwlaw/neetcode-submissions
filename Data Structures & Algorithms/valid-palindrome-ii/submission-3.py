class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        see if palindrome -> if deleting at most one char

        func check of palindrome between range

        check palindrome
            if l != r chars, then call func(l+1, r) or func(l, r-1)

        if either is true, return that
        """
        l, r = 0, len(s) - 1

        def valid(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        while l <= r:
            if s[l] != s[r]:
                return valid(l + 1, r) or valid(l, r - 1)
            l += 1
            r -= 1
        return True