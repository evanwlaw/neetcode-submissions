class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        x ^ n

        2^5 = 2^2 2^2 2


        """
        # def recurse(x,n):
        #     if x == 0:
        #         return 0
        #     if n == 0:
        #         return 1
            
        #     res = recurse(x*x, n // 2)

        #     return res if not n % 2 else res * x
        
        # result = recurse(x, abs(n))
        # return result if n >= 0 else (1/result)
        if x == 0:
            return 0
        if n == 0:
            return 1

        result = 1
        power = abs(n)

        while power:
            if power % 2: # if odd power
                result *= x
            
            x *= x
            power = power // 2

        return result if n>0 else (1/result)
