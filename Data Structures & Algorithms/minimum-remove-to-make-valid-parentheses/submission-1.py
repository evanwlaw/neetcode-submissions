class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Input: s = "nee(t(c)o)de)"
        Output: "nee(t(c)ode)"

        iterate through s
            if ( -> openBrack += 1
            if ):
                if openBrack > 1:
                    openBrack -= 1
                else: invalid
                    delete ) in s -> ) -> ""
        what's left in s is "" and valid chars
        """
        # openBrack = 0
        
        # s = list(s)
        # for i, c in enumerate(s):
        #     if c == "(":
        #         openBrack += 1
        #     elif c == ")":
        #         if openBrack >= 1:
        #             openBrack -= 1 # keep (
        #         else:
        #             s[i] = ""
        # return "".join(s)


        """
        reviewed sol
        stack to hold invalid indices
        """
        stack = []
        s = list(s)

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop() # valid
                else: # invalid close
                    s[i] = ""
        while stack: # delete invalid open
            s[stack.pop()] = ""

        return "".join(s)
        