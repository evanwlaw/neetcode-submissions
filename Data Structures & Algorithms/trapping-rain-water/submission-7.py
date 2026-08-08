class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        maxLeftHeight, maxRightHeight = 0, 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                maxLeftHeight = max(maxLeftHeight, height[l])
                output += maxLeftHeight - height[l]
                l += 1
            else:
                maxRightHeight = max(maxRightHeight, height[r])
                output += maxRightHeight - height[r]
                r -= 1
        return output
