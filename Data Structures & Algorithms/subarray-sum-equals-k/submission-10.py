class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        If our dictionary contains a previous prefix sum of, then we know there's a subarray ending here that sums to k. 

        """
        prefixMap = {0:1}
        output = runningSum = 0

        for n in nums:
            runningSum += n
            prefixSum = runningSum - k

            output += prefixMap.get(prefixSum, 0)
            prefixMap[runningSum] = 1 + prefixMap.get(runningSum, 0)
        return output
            