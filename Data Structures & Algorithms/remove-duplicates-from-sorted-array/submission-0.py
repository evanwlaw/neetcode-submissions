class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        2   10  10  30  30  30
                l
                    r
        1   2   1   3   4
            l
            r

        compare predecessors. 
        if [r] != [r - 1]: only unique if diff from prev. copy to l and incre
            l = r
            l += 1
            
        """

        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l