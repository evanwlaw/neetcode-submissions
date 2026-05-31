class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        see if board[r][c] is in the sets rows, cols, and square

        square is the 9 sub-boxes
        [0][4] -> [0][1] -> middle box
        [3][0] -> [1][0] -> second box in first col
        square[r // 3][c // 3]

        """
        rows, cols, square = defaultdict(set), defaultdict(set), defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": 
                    continue
                if ( # return false if in our sets
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in square[(r//3, c//3)]
                ):
                    return False
                
                # if we're here, it means first time seeing
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True


        
        
