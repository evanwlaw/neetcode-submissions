class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairings = {'}':'{', ')':'(', ']':'['}
        stack = []

        for bracket in s:
            if bracket in bracket_pairings: # if closed bracket
                if stack and bracket_pairings[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return not stack
