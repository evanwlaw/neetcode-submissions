class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        If our dictionary contains a previous prefix sum of, then we know there's a subarray ending here that sums to k. 

        """

        prefixDict = {0:1} # prefixSum : count
        runningTotal = 0
        output = 0

        for n in nums:
            runningTotal += n

            prefixSum = runningTotal - k

            if prefixSum in prefixDict:
                output += prefixDict[prefixSum]
            
            prefixDict[runningTotal] = 1 + prefixDict.get(runningTotal, 0)
        return output
            
