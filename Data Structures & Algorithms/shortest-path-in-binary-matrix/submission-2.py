from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        bfs
        """
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            [-1,0], [1, 0], [0,-1], [0,1],
            [-1,-1], [1, -1], [1, -1], [1,1]
        ]

        queue = deque([[0,0,1]]) # [r,c, length of path]
        grid[0][0] = 1 # mark as visited

        while queue:
            for _ in range(len(queue)):
                r, c, length = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                for dr, dc in directions:
                    cR, cC = r + dr, c + dc

                    if (cR < 0 or cR >= ROWS or
                        cC < 0 or cC >= COLS or
                        grid[cR][cC] == 1):
                        continue
                    queue.append([cR, cC, length + 1])
                    grid[cR][cC] = 1
        return -1