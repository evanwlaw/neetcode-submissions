class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(i, subset, set_sum):

            if set_sum == target:
                output.append(subset.copy())
                return
            if set_sum > target or i >= len(nums):
                return
            
            # append current i again
            subset.append(nums[i])
            dfs(i, subset, set_sum + nums[i])

            # without - popping and use next number
            subset.pop()

            dfs(i + 1, subset, set_sum)
        dfs(0, [], 0)
        return output
