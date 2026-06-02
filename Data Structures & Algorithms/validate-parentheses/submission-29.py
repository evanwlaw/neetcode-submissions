class Solution:
    def isValid(self, s: str) -> bool:
        """
        check if opening or closing brack
            if open -> add to stack
            if close -> see if it is the closing of stack[-1]
                return False if not

        can use dictionary for pairngs

        """
        pairings = {']':'[', ')':'(', '}':'{'}
        stack = []

        for c in s:
            if c in pairings:
                if stack and stack[-1] == pairings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack