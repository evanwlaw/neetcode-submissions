class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        use sets for rows, cols, and square. skip if it's '.'
        board[r][c]
        sqr[(r//3, c//3]
        """
        COLS = defaultdict(set)  # dict where each key is it's col num with the value being the numbers in it
        ROWS = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in ROWS[r] or
                    board[r][c] in COLS[c] or
                    board[r][c] in square[(r//3, c//3)]):
                    return False
                
                ROWS[r].add(board[r][c])
                COLS[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True


