class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        x = 2, n = 6 -> 64

        x = 4, n = 3 -> 64


        """
        def recursion(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = recursion(x * x, n//2)
            return res if not n % 2 else (res * x)
        
        res = recursion(x,abs(n))
        return res if n >= 0 else (1/res)