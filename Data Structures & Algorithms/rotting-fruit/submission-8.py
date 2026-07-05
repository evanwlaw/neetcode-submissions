from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''

        find num of fresh and enqueue rotten to a queue


        bfs from the rotten fruit. each level is time += 1
            each time we see a fresh fruit, change to rotten and enqueue it.
            bfs while there's still rotten fruit in queue

        '''
        ROWS, COLS = len(grid), len(grid[0])
        time, fresh = 0, 0
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    queue.append([r,c])
        
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        while queue and fresh > 0:

            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    check_r, check_c = r + dr, c + dc

                    # make sure in bound and if it's fresh
                    if (check_r >= 0 and check_r < ROWS and
                        check_c >= 0 and check_c < COLS and
                        grid[check_r][check_c] == 1
                    ):
                        fresh -= 1
                        grid[check_r][check_c] = 2
                        queue.append([check_r, check_c])
            time += 1
        return time if fresh == 0 else -1