class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        runningTotal = 0
        remainderMap = {0 : -1} # remainder value : first idx -> need first idx because need to get largest window
        
        for i, n in enumerate(nums):
            runningTotal += n
            remainder = runningTotal % k # if remainder is in map -> we've found a multiple of k

            if remainder in remainderMap and i - remainderMap[remainder] >= 2:
                return True
            
            elif remainder not in remainderMap:
                remainderMap[remainder] = i
        return False