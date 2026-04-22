class Solution:
    def isValid(self, s: str) -> bool:
        """

        ([{}])

        stack
        

        check if closed bracket
            check if  closed bracket's open and is stack[-1]:
                pop stack
        put into stack if it's an open

        dictionary = {')':'(', ']':'[', '}':'{' }
        """

        pairs = {')':'(', ']':'[', '}':'{' }
        stack = []

        for c in s:
            if c in pairs:
                # check if it's an close
                if stack and pairs[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(c)
        
        return not stack