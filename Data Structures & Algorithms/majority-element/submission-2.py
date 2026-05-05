class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        return the majority element which is n/2

        bruteforce -> dictionary value:occurrences return max -> space is O(n)

        5   5   1   1   1   5   5
        i
        count = 
        currMax = 1 

        """
        count, currMax = 0, 0

        for i in range(len(nums)):
            if count <= 0:
                currMax = nums[i]
                count = 0
            if nums[i] != currMax:
                count -= 1
            else:
                count += 1
        return currMax