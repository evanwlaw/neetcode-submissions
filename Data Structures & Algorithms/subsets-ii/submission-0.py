class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        with and without

                            []
                [1]                        []
            [1,2]     [1]             [2]      []
        [1,2,1] [1,2] [1,1]     [1]      [2]      []


        """
        output = set()
        nums.sort()
        def dfs(i, path):
            if i >= len(nums):
                output.add(tuple(path))
                return
            # with
            path.append(nums[i])
            dfs(i + 1, path)
            
            # without
            path.pop()
            dfs(i + 1, path)
            return 
            
        dfs(0, [])
        return [things for things in output]