class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {} # v : i
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in my_map:
                return [my_map[diff], i]
            my_map[nums[i]] = i


