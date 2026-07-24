class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        XOR out bits

        nums = [3,2,3]
        
        3 -> 011
        2 -> 010
        3 -> 011
        res->010 -> 2
        '''
        res = 0 # 000 is the same as 0

        for n in nums:
            res = n ^ res
        return res