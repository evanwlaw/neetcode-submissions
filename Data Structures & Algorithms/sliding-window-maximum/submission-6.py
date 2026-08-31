class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1:
            return nums

        output = []
        queue = deque()

        for i in range(len(nums)):
            # 1. eject from right smaller numbers
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            # 2. append new idx for use later (might be largest later)
            queue.append(i)

            # 3. eject previous max if out of bounds in window
            if queue[0] < i - k + 1:
                queue.popleft()
            # 4. append max value to output if window is len k
            if queue and i >= k - 1:
                output.append(nums[queue[0]])

        return output
