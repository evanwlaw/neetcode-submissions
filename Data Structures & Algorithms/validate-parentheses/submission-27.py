class Solution:
    def isValid(self, s: str) -> bool:
        """
        use stack
        """

        # init var
        pair = {')':'(', '}':'{',']':'[' }
        stack = []

        # figure out if c is open or close
        for c in s:
        # if close, see if stack[-1] is matching
            if c in pair:
                if stack and pair[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            # if open, append
            else:
                stack.append(c)

        # if stack is empty, then correct
        return not stack

