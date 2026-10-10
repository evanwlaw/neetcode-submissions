class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
                    2
                2,5
        
        can use same number multiple times
        iterate through nums:
            dfs backtrack
        
        we can do like with same nums[i] or not
        """

        output = []
        combination = []

        def dfs(i, pathSum):
            if pathSum > target or i >= len(nums):
                return
            if pathSum == target:
                output.append(combination.copy())
                return
            
            # with
            combination.append(nums[i])
            dfs(i, pathSum + nums[i])

            combination.pop()
            dfs(i + 1, pathSum)

            return
        dfs(0,0)
        return output