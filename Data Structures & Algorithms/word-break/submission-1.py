class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Input: s = "applepenapple", wordDict = ["apple","pen","ape"]
        Output: true

        find the valid segments in input matches any word in worddict
        mark the idx where it was valid -> after apple, 

        
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True # 

        for i in range(len(s)+1):
            for word in wordDict:
                if s[i-len(word) : i] == word and dp[i - len(word)] == True:
                    dp[i] = True
                    break
        return dp[len(s)]