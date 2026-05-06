class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        """

        dfs

        """
        res = []
        candidates.sort()
        def dfs(i, curr_subset, curr_val):
            if curr_val == target:
                res.append(curr_subset.copy())
                return
            if i >= len(candidates) or curr_val > target:
                return

            curr_subset.append(candidates[i])
            dfs(i + 1, curr_subset, curr_val + candidates[i])
            curr_subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates [i + 1]:
                i += 1
            dfs(i + 1, curr_subset, curr_val)
        
        dfs(0, [], 0)
        return res