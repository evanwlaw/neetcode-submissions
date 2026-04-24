class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        [7,1,7,2,2,4]

        [(start_idx, height)]

        while if stack[-1][1] > heights[i]
            pop
            maxAre = height[i] * (curr_idx - idx_popped)

            start = index


        """

        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx_popped, popped_height = stack.pop()
                maxArea = max(maxArea, popped_height * (i - idx_popped))
                start = idx_popped
            stack.append([start, h])
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


