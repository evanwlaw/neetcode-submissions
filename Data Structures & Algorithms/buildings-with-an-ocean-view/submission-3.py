class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        traverse backwards from heights - 2

        if heights[i] > heights[i+1]:
            output.append(i)
        """
        if len(heights) == 1:
            return [0]

        output = []
        maxHeight = -1
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxHeight:
                maxHeight = heights[i]
                output.append(i)
        return output[::-1]
            