class Solution:
    def isValid(self, s: str) -> bool:
        """
        Input: s = "([{}])"

        ([{}])
        
        stack: (    [   {   

        """
        stack = []
        close = {')': '(', '}': '{', ']':'['}

        for c in s:
            if c in close:
                if stack and close[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
            else:
                stack.append(c)
        return not stack
                
        