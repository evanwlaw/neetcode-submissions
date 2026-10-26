class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        return valid string
        - same number of open + close brackets.
        - delete nonvalid backets
    

        lee(t(c)o)de)
        last ) is invalid

        we need to keep track of open brackets to see if there's corresponding close

        what goes in stack?
        all chars -> if we do, then lee(t(c)o)de) works. at last ), we dont add it to stack bc we have equal open and close

        a)b(c)d -> ) -> dont add to stack bc invalid. works so far?

        ))(( -> stack should be empty at end. also works?

        a)b((c)d -> we wouldnt find that the second open bracket is invalid until we run to the end. in that case, we need to pop everything and rebuild...

        instead of stack holding chars -> hold indices of either invalid or pending validation chars.

        Two passes
        1. first pass to put possible invalid indices
            - need to track num of open bracket
            - if ( -> openBrack += 1
            - if openBrack >= 1 and char is ) -> we can pop most recent idx in stack
                else if openbrack < 1, we have invalid close bracket, so delete char
        at this point stack only has invalid 
        2. delete invalid chars from string via left over (should only be invalid open brackets left)

        a)b((c)d
        ) is deleted
        what's left in stack is idx = 3 as the other one was popped.
        stack deletes idx 3 char
        
        Time: O(N) - O(N) time for list(). Then the two passes take O(N) + O(N) time. and then final join for return is O(N). So O(4N) time that is simplified to O(N) time.

        Space: O(N) - worst case is that every char in s is an open bracket so stack will be N length -> O(N) worst case.
        """
        openBrack = 0
        stack = []
        s = list(s)

        for i, c in enumerate(s):
            if c == "(":
                openBrack += 1
                stack.append(i)
            elif c == ")":
                if openBrack >= 1: # valid close found
                    openBrack -= 1
                    stack.pop()
                else: # invalid close
                    s[i] = "" # del char
        # only invalid open bracket indices in stack left
        while stack:
            s[stack.pop()] = ""
        return "".join(s)