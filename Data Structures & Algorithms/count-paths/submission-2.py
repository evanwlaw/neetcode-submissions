class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # top down
        memo = {(0,0): 1}

        def dfs(r,c):
            if (r,c) in memo:
                return memo[(r,c)]

            
            if (r < 0 or r >= m or
                c < 0 or c >= n 
            ):
                return 0
            
            memo[(r,c)] = dfs(r - 1, c) + dfs(r, c - 1)

            return memo[(r,c)] 
        return dfs(m-1, n -1)
