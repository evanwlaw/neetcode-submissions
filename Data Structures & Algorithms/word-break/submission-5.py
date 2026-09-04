class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Input: s = "catsincars", wordDict = ["cats","cat","sin","in","car"]
        Output: false

        catsincars
        0123456789

        Iterate through s - see if current range from s[0:i] in wordDict
            - i = 3 -> we see s[0:3] is in wordDict -> cat
            - i = 4 -> we see s[0:4] is in wordDict -> cats

            - i = 6 -> we see s[3:6] and s[4:6] are in wordDict -> sin, in

            - i = 9 -> we see s[6:9] is in wordDict -> car
        

        we see that when i = 4 and i = 5, these are valid segment of valid words. 

        we see that when i = 6 this only a valid segment if there is a valid segment end at s[6 - len(curr word)]:6] -> calc that s[0:4] and/or s[0:5] are valid words

        we see that when i = 9 this only a valid segment if there is a valid segment end at s[9 - len(curr word)]:9] -> calc that s[6:9] is a valid word then s[0:4] and/or s[0:5] are valid words


        so we need to recompute valid word segments places.
        Good place to use DP - 1D. We only need to keep if that i'th place is a valid end of word. 

        dp[i] is True if s[i - len(curr word) : i] is in wordDict AND if dp[i - len(curr word) - 1] is True

        dp[0] base case is True because empty str is valid
        """


        dp = [False] * (len(s) + 1)
        dp[0] = True

        start = 0
        for i in range(len(s)):
            for word in wordDict:
                if s[i : i + len(word)] in wordDict and dp[i]:
                    if i + len(word) <= len(s):
                        dp[i + len(word)] = True

        return dp[len(s)]


