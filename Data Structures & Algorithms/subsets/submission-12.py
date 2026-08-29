class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        get subsets of nums

                                            []
                            [1]                                 []
                    [1,2]           [1]                   [2]           []
                [1,2,3] [1,2]   [1,3]      [1]      [2,3]   [2]    [3]     []
        """
        output = []
        # decision to use or not
        def dfs(i, subset):
            if i >= len(nums):
                output.append(subset.copy())
                return

            subset.append(nums[i])

            # with
            dfs(i+1, subset)
            subset.pop()

            # without
            dfs(i + 1, subset)
        dfs(0, [])
        return output