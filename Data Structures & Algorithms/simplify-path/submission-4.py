class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        return simplified path
        . is current
        .. -> go up
        // and /// -> /

        ... and .... are valid

        must start with /


        split path by / tokens

        Input: path = "/neetcode/practice//...///../courses"    

        tokens = neetcode, practice, ..., .., courses
        """
        tokens = path.split("/")
        output = []
        print(tokens)
        for t in tokens:
            if t == "..":
                if output:
                    output.pop()
                continue
            if t == "." or t =="":
                continue
            else:
                output.append(t)
        return "/" + "/".join(output)