class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
                                    []
                [1]                 [2]                 [3]
            [1,2]  [1,3]        [2,1]   [2,3]       [3,2]   [3,1]
        [1,2,3]     [1,3,2] [2,1,3]       [2,3,1] [3,2,1]   [3,1,2]
        
        
        """
        res = []
        permutation = []
        used = set()

        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return
            
            for n in nums:
                if n not in used:
                    permutation.append(n)
                    used.add(n)
                    backtrack()
                    permutation.pop()
                    used.remove(n)
        backtrack()
        return res
