class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r: int, c: int, visited: set, prevHeight: int) -> None:
            if ((r,c) in visited or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                heights[r][c] < prevHeight
            ):
                return
            
            visited.add((r,c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
        
        # dfs from first and last rows (pacific and atlantic)
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        
        # dfs from first and last cols
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        output = []

        # go through cell and see if it's in both sets
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    output.append([r,c])
        return output