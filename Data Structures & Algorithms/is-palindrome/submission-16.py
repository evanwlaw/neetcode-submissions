class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        return true/false if valid palindrome

        skip spaces and special chars
        only consider if isalnum true

        two poitners on each side
        """

        l, r = 0, len(s) - 1

        while l < r:
            # increment l and decrement r if not alnum
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # compare
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True