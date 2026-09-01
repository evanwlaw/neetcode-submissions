from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        return min time for all fresh fruit -> rotten

        there could be case where a fresh fruit is by itself and never turns rotten. At end if fresh fruit exists, then -1

        BFS outwards from rotten fruit -> turn fresh to rotten. Each "level" in bfs queue is 1 minute

        1. Get # of fresh fruits and enqueue rotten
        2. BFS from queue while # of fresh fruit > 0
            mark fresh to rotten and decrement # of fresh fruit
        3. return output minutes if # of fresh fruit == 0, else -1

        Time Complexity: O(N*M) - Where N is the num of rows and M is the num of cols. We iterate through entire grid to get the number of fresh fruits and queue up rotten -  taking O(N*M) time. And then similar time to BFS across grid from rotten fruit where in the worst case, every cell is fresh except one rotten fruit. We only visit valid fresh fruit cells and turn those rotten (we never revisit cells). Final time complexity is O(N*M).
        Space Complexity: O(N*M) - extra space is used to hold the num of fresh fruits, directions, and the queue of rotten fruit. Worst case is that every cell is rotten from the start and everything needs to be queued up. So worst space complexity is O(N*M)
        Time Spent on problem: 25 minutes
        """
        ROWS, COLS = len(grid), len(grid[0])
        output = 0
        fresh_fruits = 0
        queue = deque()
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        # 1. Get # of fresh fruits and enqueue rotten
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_fruits += 1
                elif grid[r][c] == 2:
                    queue.append([r,c])

        # 2. BFS from queue while # of fresh fruit > 0
        #     mark fresh to rotten and decrement # of fresh fruit
        while queue and fresh_fruits > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # turn fresh around rotten -> rotten
                for dr, dc in directions:
                    check_r, check_c = dr + r, dc + c

                    if (0 <= check_r < ROWS and
                        0 <= check_c < COLS and
                        grid[check_r][check_c] == 1):
                        fresh_fruits -= 1
                        grid[check_r][check_c] = 2
                        queue.append([check_r, check_c])
            output += 1

        # 3. return output minutes if # of fresh fruit == 0, else -1
        return output if fresh_fruits == 0 else -1
