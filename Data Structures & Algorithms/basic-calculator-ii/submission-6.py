class Solution:
    def calculate(self, s: str) -> int:
        """
        skip spaces
        stack -> stack[i] is with numbers to sum

        when we see a sign, we want to process the previous sign (need to have an extra sign)

        3 + 2 * 2

        stack
        3, 2 
        sign = *
        """

        prevSign = "+"
        s += "+"
        stack = []
        num = 0

        for c in s:
            if c == " ":
                continue
            elif c.isdigit():
                num = 10 * num + int(c)
            else:
                if prevSign == "+":
                    stack.append(num)
                elif prevSign == "-":
                    stack.append(-num)
                elif prevSign == "*":
                    stack.append(stack.pop() * num)
                elif prevSign == "/":
                    stack.append(int(stack.pop() / num))
                prevSign = c
                num = 0
        return sum(stack)