class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Input: nums = [2,-3,4,-2,2,1,-1,4]
        Output: 8


        nums[0:1] -> 2
        nums[0:2] -> -1
        nums[0:3] -> 3
            nums[2] is 4 which is bigger than nums[0:3]. Meaning this 4 is larger than sum of this subarray.
            we can "throw away" the current subarray and reset with this number at the ith as the new start of subarray

        Recurrence: sub_sum = max(nums[i], nums[i] + sub_sum)


        """

        sub_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            sub_sum = max(nums[i], nums[i] + sub_sum)
            max_sum = max(sub_sum, max_sum)
        return max_sum
