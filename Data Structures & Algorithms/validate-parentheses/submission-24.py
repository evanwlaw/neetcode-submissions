class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack
        ([{ 
        }

        if stack[-1] == pairs[s[i]]
            pop from stack
        """
        pairs = {'}':'{', ')':'(', ']':'['}

        stack = []

        for i in range(len(s)):
            if s[i] in pairs:
                if stack and pairs[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        return not stack