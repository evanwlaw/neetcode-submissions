class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        backtrcking
        """
        # res = []
        # permutation = []
        
        # def backtrack(i):
        #     if i == len(nums):
        #         res.append(permutation[:])
        #         return
        
        #     for j in range(i, len(nums)):
        #         permutation.append(nums[j])
        #         backtrack(j + 1)
        #         permutation.pop()
        #     return
        # backtrack(0)
        # return res
        """
        
        """
        res = []
        permutation = []
        
        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return
        
            for n in nums:
                if n not in permutation:
                    permutation.append(n)
                    backtrack()
                    permutation.pop()
            return
        backtrack()
        return res