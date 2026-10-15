class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        stack
        """

        stack = []

        for char in tokens:
            if char == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val1) + int(val2))

            elif char == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val1) * int(val2))

            elif char == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2) - int(val1))

            elif char == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2) / int(val1))
            else: # number
                stack.append(int(char))
        return int(stack[0])