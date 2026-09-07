class Solution:
    def decodeString(self, s: str) -> str:
        """
        Input: s = "2[a3[b]]c"
        Output: "abbbabbbc"


        iterating through input.
        2[a3[b

        We need to process what we have when we hit a closed bracket back up to the first open bracket.

        Stack -> while we havent hit a closed bracket, keep adding input char
        - when we hit a closed bracket, keep popping. Put to a tempstr.
        - then get the int of how many times. then add tempstr * how many times back
        
        In the end, the stack is holding a valid processed strs in between the brackets.
        """

        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else: # we hit a closed bracket
                temp_str = ""

                while stack and stack[-1] != "[":
                    temp_str = stack.pop() + temp_str
                
                stack.pop() # pop open brack
                # now get int of how many times -> k
                k = ""

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * temp_str)
        return "".join(stack)
