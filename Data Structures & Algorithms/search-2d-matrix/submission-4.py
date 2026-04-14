class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        binary search rows then cols

        

        """

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1

        while top <= bot:
            m = (top + bot ) // 2
            # look at the end of row
            # if larger then move bot
            if target > matrix[m][-1]: 
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break
        
        # if cross then not valid
        if top > bot:
            return False
        
        # get the specific row
        myrow = (top + bot) // 2
        l, r = 0, cols - 1

        while l <= r:
            middle = (l + r) // 2

            if matrix[myrow][middle] < target:
                l = middle + 1
            elif matrix[myrow][middle] > target:
                r = middle - 1
            else:
                return True
        return False