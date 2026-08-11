class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        1. hashmap for window and counts of t.
        2. brute force comparing will take too long
        3. how to use both maps to check efficiently by using the have + need
        """

        window, countT = {}, {}
        res, resLen = [-1, -1], float("inf")
        
        """
        get counts for t
        X:1 Y:1 Z:1
        """
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        """
        just need to compare this instead of compare both maps
        """
        have, need = 0, len(countT)
        l = 0

        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # we find a char from t. only increment first time we see it. 
            if char in countT and window[char] == countT[char]:
                have += 1

            while have == need:
                resultRange = r - l + 1
                if resultRange < resLen:
                    res = [l, r]
                    resLen = resultRange
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
        return s[res[0] : res[1] + 1] if resLen != float("inf") else ""
