class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def dfs(r, c):
            # base case - we hit water
            if grid[r][c] == "0":
                return False

            # mark as visited
            grid[r][c] = "0"

            for dr, dc in directions:
                check_r = r + dr
                check_c = c + dc

                if (check_r >= 0 and check_r < ROWS and
                    check_c >= 0 and check_c < COLS and
                    grid[check_r][check_c] == "1"
                ):	
                    dfs(check_r, check_c)
            return

        output = 0
        for r in range(ROWS):
            for c in range(COLS):
                # found an island
                if grid[r][c] == "1":
                    output += 1
                    dfs(r, c)
        return output
