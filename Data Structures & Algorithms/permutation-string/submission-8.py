class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        so pretty much, we need a window of 3 that slides across s2. this window is size s1.

        window needs to hold the current variables of len(s1)

        Input: s1 = "abc", s2 = "lecabee"
        Output: true

        curr window:
        l   e   c
        right now, we do know the current letters in the window
        - We do know that there is one letter from s1 in this current window (c).
        - We know that of the 3 letters, we do have 1 letter already. 
        

        next iteration, slide to "a"
        curr window:
        e   c   a
        we do know the current letters in the window
        - We do know that there is 2 letter from s1 in this current window (c, a).
        - We know that of the 3 letters, we do have 2 letter already. 

        next iteration, slide to "b"
        curr window:
        c   a   b
        we do know the current letters in the window
        - We do know that there is 3 letter from s1 in this current window (c, a, b).
        - We know that of the 3 letters, we do have 3 letter already. 

        terminate return True

        ex2:
        Input: s1 = "abc", s2 = "lecaabee"
        Output: false

        curr window:
        l   e   c
        we do know the current letters in the window
        - We do know that there is one letter from s1 in this current window (c).
        - We know that of the 3 letters, we do have 1 letter already. 
        
        next iteration, slide to "a"
        curr window:
        e   c   a
        we do know the current letters in the window
        - We do know that there is 2 letter from s1 in this current window (c, a).
        - We know that of the 3 letters, we do have 2 letter already. 


        next iteration, slide to "a"
        curr window:
        c   a   a
        we do know the current letters in the window
        - We do know that there is 3 letter from s1 in this current window (c, a).
        - We know that of the 3 letters, we do have 2 letter already. but the second "a" is not considered the 3rd letter we're looking at
        - we do not have a way to check how many letters are needed from s1 are in current window


        Needed variables per iteration:
        - Number of chars needed
        - Number of chars are in current window that are the ones we needed from s1 (and should not increment more than what we need)
        - hashmaps -> char : count
            - current window chars
            - s1 chars
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == window:
            return True

        for r in range(len(s1), len(s2)):
            window[ord(s2[r - len(s1)]) - ord('a')] -= 1
            window[ord(s2[r]) - ord('a')] += 1
            if s1_count == window:
                return True


        return False