class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        n = the num of open brackets
        n = 3

                                        (
                            ((                  ()
                    (((          (()         ()(
                ((()         (()(  (())
            ((())          (()()    
        ((()))          (()())

        if open == close == n -> it's a valid path
        if open < n -> add another open bracket
        if open > close -> add close brack


        '''
        stack = []
        res = []

        def dfs(openB: int, closeB: int):
            if openB == closeB == n:
                res.append(''.join(stack))
                return

            if openB < n:
                stack.append('(')
                dfs(openB + 1, closeB)
                stack.pop()
            if openB > closeB:
                stack.append(')')
                dfs(openB, closeB + 1)
                stack.pop()

        dfs(0, 0)
        return res