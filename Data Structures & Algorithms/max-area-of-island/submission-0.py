class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        iterate through grid.
            if cell is "1", we found island
                dfs to get area

        """
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r,c, area):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0):
                return 0
            
            grid[r][c] = 0
            area += 1
            search =(
                dfs(r - 1, c, area) +
                dfs(r + 1, c, area) +
                dfs(r, c - 1, area) +
                dfs(r, c + 1, area)
            )
            return search + 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(dfs(r,c, 0), max_area)

        return max_area