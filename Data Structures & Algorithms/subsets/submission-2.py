class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        1, 2, 3

                                    []
                    [1]                       []         
            [1,2]          [1]          [2]         []    
        [1,2,3] [1,2]  [1,3]  [1]    [2,3]  [2]  [3]    []
        
        
        '''

        res = []

        def dfs(path: List[int], idx: int) -> None:
            # base case
            if idx == len(nums):
                res.append(path.copy())
                return

            # with
            path.append(nums[idx])
            dfs(path, idx + 1)

            #without
            path.pop()
            dfs(path, idx + 1)
        dfs([], 0)
        return res
