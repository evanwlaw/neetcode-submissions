class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = {0:1} # prefix sum : count occ
        runningTotal = 0
        output = 0
        for n in nums:
            runningTotal += n

            prevSlice = runningTotal - k

            if prevSlice in sumMap:
                output += sumMap[prevSlice]
            sumMap[runningTotal] = 1 + sumMap.get(runningTotal, 0)
        return output
