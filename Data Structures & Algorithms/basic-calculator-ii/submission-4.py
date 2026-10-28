class Solution:
    def calculate(self, s: str) -> int:
        """
        3+2*2-2 -> 3 + 4 - 2

        ideally if we can eval * and / first then sum/minus the rest.

        use stack?
        keep sum/minus (if -, then put negative) in it and eval * / on first pass. Then return sum(stack)

        3+2*2-2 

        stack = 3

        track sign before operand
        sign = + # default to + to add first num to stack
        num = 0 # num in string can be multi digit

        
        iterate through s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == " ":
                continue
            elif sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(int(stack.pop() / num))
            else:
                sign = c
                num = 0
        return sum(stack)
        """
        stack = []
                # track sign before operand
        sign = "+" # default to + to add first num to stack
        num = 0 # num in string can be multi digit
        s += "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == " ":
                continue
            else: 
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0
        return sum(stack)