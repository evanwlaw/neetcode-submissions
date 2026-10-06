class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        with and without

                            []
                [1]                        []
            [1,2]     [1]             [2]      []
        [1,2,1] [1,2] [1,1]     [1]      [2]      []
        """
        output = []

        def dfs(i, path):
            if i >= len(nums):
                output.append(path.copy())
                return
            # with
            path.append(nums[i])
            dfs(i + 1, path)
            
            # without
            path.pop()
            dfs(i + 1, path)
            return 
            
        dfs(0, [])
        return output