class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        return combinatino of numbers that add up to target

        we can use multiples of each nums[i]

                [2]     []
            [2,2]      []

        backtrack
            if currSum > target:
                return
            if currSum == target:
                subset -> append to output
        

        """


        res = []
        subset = []

        def backtrack(i, currSum):
            if i == len(nums) or currSum > target:
                return
            if currSum == target:
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i, currSum + nums[i])

            # without same int
            subset.pop()
            backtrack(i + 1, currSum)

            return
        backtrack(0, 0)

        return res
            