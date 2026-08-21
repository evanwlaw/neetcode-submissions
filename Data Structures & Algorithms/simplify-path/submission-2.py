class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        . -> curr dir
        .. -> prev dir (one lvl up)
        // and /// or /////// -> single /
        ... or .... (anything past two ..) is valid dir name

        output is simplified canonical path:
            - path starts /
            - dir must be sep by one /
            - path should not have . or ..

        
        Input: path = "/..//_home/a/b/..///"
        Output: "/_home/a"

        iterate through input path
        path[0] = / -> we see this string. if we move on, won't know if it's just a single dash or multiple dashes. we know we need this in final output bc it's valid start.
        
        next iteration path[1] = .
        we see this string. if we move on, won't know if it's just a single dot or multiple dots. if it's single dot, we can "ignore" it in final output

        next iteration path[2] = .
        we see this string. if we move on, won't know if it's just a single dot or multiple dots. if prev is a dot, and this is a dot, we know we can remove these two dots plus the previous element if it's not the first sladh

        next iterationpath[3] = /
        we see this string. if we move on, won't know if it's just a single dash or multiple dashes. we know we need at least one in final output bc it's valid slash.

        next iterationpath[4] = /
        we see this string. if we move on, won't know if it's just a single dash or multiple dashes. we know we need at least one in final output bc it's valid slash. but since it's second one seen, we can do not keep this.

        next iterations is for _home...
        we need a way to keep these together as they're valid dir name

        next iterations for /a
        need to hold these. if we don't, then we lose the dir

        next iterations for/b
        need to hold these. if we don't, then we lose the dir

        next iteration is for ..
        need to hold these and then remove previous folder for /b because we went up one dir. if we don't, then we are in the wrong dir

        next iterations are for ///
        need to turn these into / but since it's last one, we can remove it.


        So it seems a stack is the easiest way to hold things as we iterate through the input path.

        We need a temp variable to hold the token/directory.
        After processing each char in the intput path, each value of the stack holds the current valid tokens of the final output path.
        If in temp token var is .., then we pop the last token in the stack

        piece everything togeth from stack -> return "/" + "/".join(stack)
        """

        curr_token = ""
        stack = []

        for c in path + "/":
            if c == "/":
                if curr_token == "..":
                    if stack:
                        stack.pop()
                elif curr_token != "" and curr_token != ".":
                    stack.append(curr_token) 
                curr_token = ""
            else:
                curr_token += c
        print(stack)
        return "/" + "/".join(stack)