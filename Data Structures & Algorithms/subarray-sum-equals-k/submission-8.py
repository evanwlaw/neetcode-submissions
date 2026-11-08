class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        sequential 

        """
        prefixDict = {0:1} # prefixSum : count
        prefixSum = output = 0

        for n in nums:
            prefixSum += n
            check = prefixSum - k 
            if check in prefixDict:
                output += prefixDict[check]
            
            prefixDict[prefixSum] = 1 + prefixDict.get(prefixSum, 0)
        
        return output