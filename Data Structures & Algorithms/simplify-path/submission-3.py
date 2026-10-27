class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        use stack. each stack is valid 
        

        if c == / and stack[-1] == / -> keep going
        if c == .. -> pop 

        can split path by / and process tokens
        """
        tokens = path.split("/")
        stack = []

        for t in tokens:
            if t == "..":
                if stack:
                    stack.pop()
            elif t != "" and t != ".":
                stack.append(t)
        return "/" + "/".join(stack)