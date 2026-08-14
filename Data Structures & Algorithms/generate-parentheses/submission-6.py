class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        use stack


        use open and close to track how many parenthesis used

        invalid if open > n or close > open.

        add open if open < n.

        (((()

        add close if close < open.
        """

        output = []
        stack = []
        def dfs(open, close):
 
            if open == n and close == open:
                output.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                dfs(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                dfs(open, close + 1)
                stack.pop()

        dfs(0,0)
        return output
            