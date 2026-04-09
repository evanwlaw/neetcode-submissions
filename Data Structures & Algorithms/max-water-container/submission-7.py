class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """

        two ptrs l, r
        length = r - l + 1
        area = length * min(heights[l], heights[r])
        res = max(res, area)

        move the smaller ptr
        """

        l,r = 0, len(heights) - 1

        res = 0

        while l < r:
            length = r - l
            max_water = length * min(heights[l], heights[r])

            res = max(res, max_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
