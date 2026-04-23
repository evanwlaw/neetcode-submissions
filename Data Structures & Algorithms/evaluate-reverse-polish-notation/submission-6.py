class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        stack

        1   2

        check if token[i] is an op

            if token[i] == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif token[i] == '-'
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif token[i] == '*'
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif token[i] == '/'
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a / b)

        if num, append to stack
        3   3   *
        """
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif tokens[i] == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            elif tokens[i] == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif tokens[i] == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a / b)
            else:
                stack.append(int(tokens[i]))

        return int(stack[-1])


