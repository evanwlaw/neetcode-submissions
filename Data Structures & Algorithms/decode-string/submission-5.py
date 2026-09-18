class Solution:
    def decodeString(self, s: str) -> str:
        """
        Input: s = "2[a3[b]]c"
        Output: "abbbabbbc"

        So we cant process the entire 'a' until we we process the substring inside 'b'

        stack would be a good data structure to use.

        push char to stack until we hit a closed bracket
            2[a3[b is in the stack until we hit the first closed bracket

            build the substring
            get the int
            
            multiply substring by int
            push completed substring back to stack then keep adding chars back to stack

        stack[i] will hold chars until processing closed brackets.

        after processing all closed brackets, stack will contain all valid and processed substrings. We just append those together

        AFter processing b, the stack would look like
        Stack
        [2,[,a,bb]]


        """

        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                # we hit closed bracket, build substring
                substring = ""
                while stack and stack[-1] != "[":
                    substring = stack.pop() + substring

                # pop open bracket
                stack.pop()

                # get int
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                # multiply and append
                stack.append(int(k) * substring)
        return "".join(stack)