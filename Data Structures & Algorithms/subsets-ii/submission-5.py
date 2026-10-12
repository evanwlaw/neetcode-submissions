class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """ 
        return subsets of given array nums

        nums may include duplicates
        output may NOT have duplicate subsets

        backtrack

                            []
                    [1]                     []
            [1,2]       [1]             [2]     []
        [1,2,1] [1,2] [1,2] [1]

        using the backtrack of with/without will get duplicates

        we can sort the input nums -> O(nlogn) time but time is dominated still by the backtrack -> 2 options for every i in nums. O(N*2^N) 

        when we pop in backtrack, we want to skip the same i
        check to see the next i is in bounds and if it's the same as i -> keep incrementing
        """
        nums.sort()
        res = []
        subset = []
        def backtrack(i):
            nonlocal res

            if i == len(nums):
                res.append(subset[:])
                return

            # with 
            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i + 1)
            return
        backtrack(0)
        return res
