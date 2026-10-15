class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        * can be ) or ( or empty string


        track: open and close brackets

        if we see ( -> increment open

        ((**)

        open = 2
        close = 1
        wild = 2
        """

        """
        reviewed neetcode solution

        Track how many open left brackets there are and the max number of left brackets there are if wildcard is an open bracket

        Seeing ( alwasy increase open
               ) always decrease open
               * could increase
        """
        leftMin, leftMax = 0,0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else: # it's a wildcard
                leftMin -= 1 # it could be used as closed so decrease the min open we have
                leftMax += 1

            if leftMax < 0: # if we ever encounter leftMax is negative, it's invalid
                return False   # (*)( is not valid
            if leftMin < 0:
                leftMin = 0 # reset leftmin if we go negative due to *
        return not leftMin
