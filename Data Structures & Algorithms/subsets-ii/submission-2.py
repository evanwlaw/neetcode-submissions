class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Input: nums = [1,2,1]
        Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

                                            []  
                            [1]                             []
                    [1,2]           [1]             [2]          []
                [1,2,1] [1,2] [1,1]       [1]     [1,2]
        Use DFS
        If we were to iterate as is, then we'd get dupe subset. Which is fine if we were to append to an output set. Time complexity is O(N * 2^N) -> there are 2^N total subsets choices that we need to explore where each subset could be length N.

        We could also sort the intput array -> same algorithm of include/or not. Difference is that when we travers, if current nums[i] is the same as nums[i + 1], then we can just continue.

        The sort is O(N logN) but the O(N* 2^N) exploration is still dominant and in practice would run less as we'd skip duplicates

        [1,1,2]
                                []
                    [1]                           []
            [1,1]           [1]             [2]           []
        [1,1,2] [1,1]  [1,2]    [1]         
        """
        nums.sort()
        output = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                output.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)
            
            return
        dfs(0)
        return output

            
