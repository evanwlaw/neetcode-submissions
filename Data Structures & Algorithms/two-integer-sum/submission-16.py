class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if not nums or target == None: # return empty if invalid inputs
        #     return []

        seen_hashmap = {}  # num_val : idx

        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in seen_hashmap:
                return [seen_hashmap[difference], i]
            else:
                seen_hashmap[nums[i]] = i
        return [] # return empty list if no solution found