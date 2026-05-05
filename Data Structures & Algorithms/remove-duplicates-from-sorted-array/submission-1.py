class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        2   10  10  30  30  30
                    i
                r

        2   10  30


        1   1   2   3   4
        
        1   2   3   4

        return k -> the number of unique elements. ex1 is 3 ex2 is 4
        keep r as the frontier -> overwrite when we find a unique element to replace
        """


        r = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[r] = nums[i]
                r += 1
        return r