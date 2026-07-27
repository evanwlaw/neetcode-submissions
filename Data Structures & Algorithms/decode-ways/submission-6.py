class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        0123
        1012
        
        '''
        if not s or s[0] == "0":
            return 0
        n = len(s) + 1
        prev2 = 1
        prev1 = 1
        
        for i in range(2, n):
            temp = 0
            digit = int(s[i - 1])
            if digit > 0:
                temp += prev1

            digit = int(s[i - 2 : i])
            if 10 <= digit <= 26:
                temp += prev2
            prev2 = prev1
            prev1 = temp
        return prev1
