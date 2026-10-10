class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        we want to count number of islands.
        
        iterate through grid,
            if we see 1, dfs
                increment island seen by 1
                dfs mark all islands as 0 so we dont revisit.
        """

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1,0], [0,-1],[0,1]]
        res = 0

        def dfs(r, c):
            # if grid[r][c] != "1":
            #     return
            grid[r][c] = "0"

            for dr, dc in directions:
                checkR, checkC = dr + r, dc + c
                if (0 <= checkR < ROWS and
                    0 <= checkC < COLS and
                    grid[checkR][checkC] == "1"
                ):
                    dfs(checkR, checkC)
            return
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r,c)
        return res