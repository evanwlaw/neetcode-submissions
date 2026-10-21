class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        we want to delete invalid idx's in s

        use a stack where stack[i] is invalid idx in s that we need to delete

            append open bracket char idx to stack then pop if valid.
        
            remove close brackets in our string 


        Input: s = "nee(t(c)o)de)"
        Output: "nee(t(c)ode)"

        n   e   e   (   t   (   c   )   o   )   d   e   )
        0   1   2   3   4   5   6   7   8   9   10  11  12
        
        stack

        skip chars.
        if open, append idx to stack to check if valid
        if close,
            if stack is nonempty, means we have a valid open bracket. pop open bracket from stack
            else:
                mark the close bracket in string as "" -> not valid
        
        what's left in stack is open brackets to be deleted
        while stack:
            s[stack.pop()] = ""

        """

        s = list(s)
        stack = []
        
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        while stack:
            s[stack.pop()] = ""
        
        return "".join(s)