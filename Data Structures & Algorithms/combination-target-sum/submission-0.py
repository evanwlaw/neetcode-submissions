class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
                                                []
                                    [2]                             []
                        [2,2]                  [2]             [5]          []
                [2,2,2]         [2,2]      [2,6]  [2]                    [6]     []
        [2,2,2,2]   [2,2,2] [2,2,5]  [2,2]
        """

        res = []

        def dfs(i, curr_subset, total_val):
            if total_val == target:
                res.append(curr_subset.copy())
                return
            if i >= len(nums) or total_val > target:
                return

            curr_subset.append(nums[i])
            dfs(i, curr_subset,total_val + nums[i]) # try using the same number

            curr_subset.pop()
            dfs(i + 1, curr_subset, total_val) # check adding the next val in array
        dfs(0, [], 0)
        return res
