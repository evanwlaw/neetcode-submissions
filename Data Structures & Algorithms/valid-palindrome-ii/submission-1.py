class Solution:
    def validPalindrome(self, s: str) -> bool:
        """

        two ptrs at each end of string -> if not same...
        
            see if next s[l] == s[r-1]:
                    move r = r - 2 places
                elif s[l+1] == s[r]:
                    move l = l + 2 places
                else:
                    return False bc has to be more than 1 char

        Input: s = "abbadc"
        Output: false


        """
        # l, r = 0, len(s) - 1

        # while l <= r:
        #     if s[l].lower() != s[r].lower():
        #         if s[l] == s[r - 1]:
        #             r = r - 2
        #         elif s[l + 1] == s[r]:
        #             l = l + 2
        #         else:
        #             return False
        #     else:
        #         l += 1
        #         r -= 1
        # return True

        """
        Reviewed neetcode.
        I was on the right track.

        Even better, make valididating palindrom a sep function. then if go through s, find difference, then validate the part of string -/+ 1
        
        """

        def validate(s, left, right):
            while left <= right:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
            return True

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l].lower() != s[r].lower():
                return validate(s, l + 1, r) or validate(s, l, r - 1)
            else:
                l += 1
                r -= 1
        return True