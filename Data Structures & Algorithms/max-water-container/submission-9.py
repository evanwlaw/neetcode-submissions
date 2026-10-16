class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        two ptrs at ends

        we're constrained by shortest height bar -> move that

        area = (r - l) * min(heights[l], heights[r])
        """

        maxWater = 0
        l, r = 0, len(heights) - 1

        while l <= r:
            area = (r - l) * min(heights[l], heights[r])
            maxWater = max(maxWater, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
            
