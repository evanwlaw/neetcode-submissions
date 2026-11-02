class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1

        res = 1
        power = abs(n)

        while power:
            if power & 1: # if odd num
                res *= x # multiply itself
            x *= x
            power >>= 1 # divide power by half with bitwise
        return res if n >= 0 else (1/res)
        
                