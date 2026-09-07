class Solution:
    def decodeString(self, s: str) -> str:
        """
        Input: s = "2[a3[b]]c"
        Output: "abbbabbbc"

        abbbabbb


        Input: s = "axb3[z]4[c]"
        Output: "axbzzzcccc"

        cccc
        zzz
        axb


        Input: s = "ab2[c]3[d]1[x]"
        Output: "abccdddx"

        stack:   
        ab2[c

        Stack holds all values that's not a closing bracket.

        Rules:
        1. append to stack while not "]"
        2. When we hit close bracket -> pop/build substr until open bracket "["
            substr -> c
        3. now get integer how many times need to append substr back to stack

        return stack as ans
        
        """
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            
            # now we hit a close -> build substr until open
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr # insert at front of substr
                # pop open bracket
                stack.pop()
                
                # now get integer
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        
        return "".join(stack)

