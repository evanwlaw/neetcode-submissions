class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Input: nums = [1,2,3]

                                []
                        1       2         3
                12      13   21      23  31 32
            123         132 213     231  312    321

        All values in input are unique.
        backtrack -> iterate through n while it's not in our current permuation
        """

        output = []
        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                output.append(permutation[:])
                return
            
            for n in nums:
                if n not in permutation:
                    permutation.append(n)
                    backtrack()
                    permutation.pop()
            return
        
        backtrack()
        return output