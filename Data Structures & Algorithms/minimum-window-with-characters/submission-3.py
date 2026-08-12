class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """

        sliding window -> use two hashmaps, window and the letter count for t
        Keep track if window has the chars in t (use var "have" vs "need")

        Need to keep track l,r -> need to return substring of s or "" if invalid
        Also need to track the min window of valid result range

        1. Get count of chars in t to map countT

        2. iterate through str s.
            increase window size

        """

        window, countT = {}, {}
        
        # 1. Get count of chars in t to map countT

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        l = 0
        res, res_len = [-1,-1], float("inf")

        # 2. iterate through str s.
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            # incr have if it's part of countT and if seeing first time
            if char in countT and window[char] == countT[char]:
                have += 1
            
            # pop from left if have == need, we have found res
            while have == need:
                # update res
                res_range = r - l + 1
                if res_range < res_len:
                    res_len = res_range
                    res = [l, r]
                window[s[l]] -= 1 # pop left

                # check if we have popped a necessary char
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
        return s[res[0] : res[1] + 1] if res_len != float("inf") else ""
                



