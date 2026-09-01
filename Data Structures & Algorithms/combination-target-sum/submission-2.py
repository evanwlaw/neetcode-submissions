class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        subset = []

        def dfs(i, curr_sum):
            if curr_sum > target or i >= len(nums):
                return
            if curr_sum == target:
                output.append(subset.copy())
                return
            
            # with
            subset.append(nums[i])
            dfs(i, curr_sum + nums[i])
            subset.pop()

            # without
            dfs(i + 1, curr_sum)


        
        dfs(0, 0)

        return output

            