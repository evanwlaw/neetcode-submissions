class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        if len()
        if openBrack < n -> add open backet
        if openBrack > closeBrack -> add close bracket

        '''
        output = []
        path = []

        def dfs(openBracket, closeBracket):
            if openBracket == closeBracket == n:
                output.append(''.join(path))
                return 
            
            if openBracket < n:
                path.append('(')
                dfs(openBracket + 1, closeBracket)
            
                path.pop()
            if openBracket > closeBracket:
                path.append(')')
                dfs(openBracket, closeBracket + 1)
                path.pop()
        
        dfs(0, 0)
        return output
