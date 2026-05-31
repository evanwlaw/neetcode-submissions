class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dictionary = {}

        for i in range(len(nums)):
            check_sum = target - nums[i]
            if check_sum in my_dictionary:
                return [my_dictionary[check_sum], i]
            my_dictionary[nums[i]] = i
        return []