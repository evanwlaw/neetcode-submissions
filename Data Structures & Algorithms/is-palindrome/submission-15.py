class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Input: s = "Was it a car or a cat I saw?"
        Output: true

        so have two ptrs at each end and compare
            l at [0] -> W
            r at [len(s) - 1] -> ?

            We need to iterate r because it's not a letter
                Iterate l and r while they're not letters
            l[0] needs to be lowercase -> so if letter, make sure it's lower case
            


        """

        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True