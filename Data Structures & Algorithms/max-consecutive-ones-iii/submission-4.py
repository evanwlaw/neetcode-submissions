class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        1   1   1   0   0   0   1   1   1   1   0
        ----------------
        k = 2 -> flip at most k
        sliding window
        - increase if numFlipped <= k
        - move left while numFlipped > k
            if nums[l] == 0 -> numFlipped -= 1
        """

        numFlipped = 0
        l = 0
        maxWind = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numFlipped += 1

            while numFlipped > k:
                if nums[l] == 0:
                    numFlipped -= 1
                l += 1
            maxWind = max(maxWind, r - l + 1)

        return maxWind
