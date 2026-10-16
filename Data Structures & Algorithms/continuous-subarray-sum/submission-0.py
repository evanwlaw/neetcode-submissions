class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        review neetcode solution. i thought of using sliding window but didnt seem like it was efficient. good thing i reviewed bc seems even neetcode had issues deriving the solutioon

        Use a running total sum to calculate the prefix sums. Use hashmap to show the remainders we've seen. If we've seen the same remainder before, then it means we found prefixSum that is summed by a number divisible by k


        if prefixSum % k == 0 -> then we found solutiono
        if prefixSUm % k is found exists in our hashmap already, then we found a solution

        edge case:
            first num is 0 -> 0 is a multiple of k

        """

        remainder = { 0 : -1} # remainder : idx 
        total = 0

        for i, n in enumerate(nums):
            total += n
            r = total % k

            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] >= 2: # check to see that subarray is 2
                return True
        return False