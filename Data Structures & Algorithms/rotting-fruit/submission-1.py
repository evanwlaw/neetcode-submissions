from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0,0
        queue = deque()

        # prework. find the num of fresh. put rotten cord into q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # num of fresh
                    fresh += 1
                if grid[r][c] == 2: # rotten
                    queue.append([r,c])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        while queue and fresh > 0:

            for i in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    check_r, check_c = r + dr, c + dc

                    if (0 <= check_r < ROWS and 0 <= check_c < COLS and grid[check_r][check_c] == 1 ):
                        fresh -= 1
                        grid[check_r][check_c] = 2
                        queue.append([check_r, check_c])
            time += 1
            
        return time if fresh == 0 else -1