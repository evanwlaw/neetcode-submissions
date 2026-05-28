class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = {} # num : idx

        for i in range(len(nums)):
            check_num = target - nums[i]
            if check_num in my_list:
                return [my_list[check_num], i]
            my_list[nums[i]] = i