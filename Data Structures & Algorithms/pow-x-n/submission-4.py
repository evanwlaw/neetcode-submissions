class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1

        res = 1
        power = abs(n) # could be negative power
        
        while power:
            if power & 1: # odd power
                res *= x
            
            # even
            x *= x
            power >>= 1
        
        return res if n > 0 else (1/res)
            