class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """

        return all subsets. 
        input may contain duplicates
        output canNOT contain duplicate subsets

        dfs -> include or dont include

                         []
                [1]                 []
            [1,2]  [1]          [2]     []
        [1,2,1]      [1]   [2, 1]      [1]

        this wouldnt work due -> dupes

        what if we sorted the input nums first?
        we can skip seen num[i].

        only dfs next if i < len(nums) and nums[i] == nums[i+1]:
            keep incrementing i while they're the same so we can skip dupe

        1 1 2
                []
            [1]     []
        [1,1] [1]  [2]  []
        """
        nums.sort()
        output = []
        subset = []

        def dfs(i):
            if i == len(nums):
                output.append(subset.copy())
                return
            
            # with
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # without
            dfs(i + 1)
            return
        dfs(0)
        return output
