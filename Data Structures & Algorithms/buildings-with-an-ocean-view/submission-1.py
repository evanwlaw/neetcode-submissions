class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        return list of indices that are able to see the ocean / not blocked by a higher heights to it's right


        Input: heights = [9,8,7,7,6,5,4,3]
        Output: [0,1,3,4,5,6,7]
        
        0   1   2   3   4   5   6   7
        9   8   7   7   6   5   4   3

        O   O       O   O   O   O   O

        can greedily add from right
        """
        output = []
        tallest = -1
        for i in range(len(heights) - 1, -1, -1):
            # tallest = max(tallest, heights[i])
            if tallest < heights[i]:
                output.append(i)
                tallest = heights[i]
        return output[::-1]