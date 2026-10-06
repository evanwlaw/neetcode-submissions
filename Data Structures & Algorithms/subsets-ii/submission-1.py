class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        with and without

                            []
                [1]                        []
            [1,2]     [1]             [2]      []
        [1,2,1] [1,2] [1,1]     [1]      [2]      []


        """
        output = []
        nums.sort()
        def dfs(i, path):
            if i >= len(nums):
                output.append(path.copy())
                return
            # with
            path.append(nums[i])
            dfs(i + 1, path)
            
            # without
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            dfs(i + 1, path)
            return 
            
        dfs(0, [])
        return [things for things in output]