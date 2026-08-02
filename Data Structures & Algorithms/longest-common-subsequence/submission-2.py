class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        m, n = len(text1), len(text2)
        def longest(i, j):
            if i == m or j == n:
                return 0
            
            if (i, j) in memo:
                return memo[(i,j)]
            

            elif text1[i] == text2[j]:
                memo[(i,j)] = 1 + longest(i + 1, j + 1)
            
            else:
                memo[(i,j)] = max(longest(i + 1, j), longest(i, j + 1))
            return memo[(i, j)]
        return longest(0,0)