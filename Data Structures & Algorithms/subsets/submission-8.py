class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
                            []
                    [1]             []
            [1,2]       [1]     [2]     []
        ..
        '''
        output = []
        path = []
        def dfs(curr_path, i):

            if i == len(nums):
                output.append(curr_path.copy())
                return

            #with
            curr_path.append(nums[i])
            dfs(curr_path, i + 1)

            #without
            curr_path.pop()
            dfs(curr_path, i + 1)
            return
        dfs([], 0)
        return output

