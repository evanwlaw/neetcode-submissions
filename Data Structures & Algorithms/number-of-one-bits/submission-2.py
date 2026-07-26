class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        0000010111 % 2 -> 1
         000001011 >> 1
         000001011 % 2 -> 1
          00000101 >> 1
          00000101 % 2 -> 1
        '''
        res = 0

        while n:
            res += n % 2
            n = n >> 1
        return res

    