class Solution:
    def calculate(self, s: str) -> int:
        """
        skip spaces

        put into stack -> sum all nums in stack at the end
        track the sign before an operand

        need to add something at s so we can go through each char

        each loop -> reset num and update sign
        """
        num = 0
        preOp = "+"

        s += "+"
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c) # could be non single digit, move left
            
            elif c == " ": #skip space
                continue
            else: # it's a sign
                if preOp == "*":
                    stack.append(stack.pop() * num)
                elif preOp == "/":
                    stack.append(int(stack.pop()/num))
                elif preOp == "-":
                    stack.append(-num)
                elif preOp == "+":
                    stack.append(num)

                num = 0
                preOp = c
        return sum(stack)