class Solution:
    def myPow(self, x: float, n: int) -> float:
        """

        return x raised to n. no builtin lib functions

        recurse

        """
        
        def recurse(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = recurse(x * x, n // 2)
            return res * x if n % 2 else res # if n is odd vs even
            
        output = recurse(x, abs(n))
        return output if n >= 0 else (1 / output)
