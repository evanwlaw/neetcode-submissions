class Solution:
    def calculate(self, s: str) -> int:
        """
        skip spaces
        
        use a stack
        2
        2
        3

        pop when we see a *-/

        pu
        """
        num = 0
        preSign = "+"
        s += "+"
        stack = []

        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == " ":
                continue
            else: # if not num, then it's a sign
                if preSign == "+":
                    stack.append(num)
                elif preSign == "-":
                    stack.append(-num)
                elif preSign == "*":
                    stack.append(stack.pop() * num)
                elif preSign == "/":
                    stack.append(int(stack.pop() / num))
                
                num = 0
                preSign = c
        
        return sum(stack)

