from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        iterate through grid 
            if we find a 1:
                increment num of islands.
                dfs

        dfs through island
            change each 1 into 0 as we've seen it

        '''

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        res = 0

        
        def dfs(r,c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == "0"
            ):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        return res