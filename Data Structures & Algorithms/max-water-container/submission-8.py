class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        result -> max amt of water

        two ptrs at 0 and len(heights) - 1

        length = r - l
        area = length * min(heights[l], heights[r])
        max_result = max(max_result, area)

        increment l or r where heights[l/r] smaller
        """

        max_result = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            max_result = max(max_result, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_result