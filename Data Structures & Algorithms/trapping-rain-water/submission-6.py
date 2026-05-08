class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        max_area = 0

        while l < r:
            
            # l bar is smaller
            if height[l] < height[r]:
                l += 1
                left_max = max(left_max, height[l])
                max_area += left_max - height[l]

            # r bar is smaller
            else:
                r -= 1
                right_max = max(right_max, height[r])
                max_area += right_max - height[r]
        return max_area