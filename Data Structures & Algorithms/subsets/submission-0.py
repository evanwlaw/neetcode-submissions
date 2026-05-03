class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        dfs backtracking

        basecase -> if i >= len(nums) return res.append(subset.copy())
        """

        res = []
        subset = []

        def dfs(i):
            if i >= len(nums): return res.append(subset.copy())

            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res