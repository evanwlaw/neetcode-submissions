class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack

        if we see an open -> append to stack
        if we see a close and stack is nonempty -> pop

        return not stack
        """
        bracketPairs = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            # close
            if c in bracketPairs:
                if stack and stack[-1] == bracketPairs[c]: # matching 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack