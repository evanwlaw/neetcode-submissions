class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        grid is sorted in non-decreasing order already

        [1    2    4    8]
        [10   11   12   13]
        [14   20   30   40]
        Target = 10

        first binary search which row it's in
            m = (Top Row + Bottom Row) // 2
            if matrix[m][0] <= target <= matrix[m][-1] -> target is possible in row m

            if target < matrix[m][0] -> target is smaller than in row m
                bottom row = m - 1
            else -> target > matrix[m][-1] -> target is larger than in row m
                top row = m + 1
        
        second binary search on the row
        """

        top, bottom = 0, len(matrix) - 1

        checkRow = -1

        while top <= bottom:
            m = top + (bottom - top) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                checkRow = m
                break
            
            if target < matrix[m][0]: # target is smaller than in row m
                bottom = m - 1
            else: # target is larger than in row m
                top = m + 1
        
        if checkRow == -1: # number is not found in current grid
            return False
        
        l, r = 0, len(matrix[checkRow]) - 1

        while l <= r:
            m = l + (r - l) // 2

            if matrix[checkRow][m] == target:
                return True
            
            if target < matrix[checkRow][m]:
                r = m - 1
            else:
                l = m + 1
        return False
                
