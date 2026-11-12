class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        need to check if current substr == one of the words in worddict.
            - also need to check if previous ones were divisible into valid words
        dp[i] = up to i, we can segment in to words in worddict
        dp[0] = True - seed empty
        """
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDict = set(wordDict)

        for i in range(len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
        return dp[len(s)]
