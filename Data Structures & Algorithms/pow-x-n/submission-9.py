class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        x = 2
        n = 6

        2^6 = 4^3 = 64

        3^4 = 9^2

        2^5 = 2 * 2^2 * 2^2 = 2 * 4^2 = 32

        x *= x and n // 2

        if n % 2 -> odd, then result *= x
        """

        def recurse(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1

            res = recurse(x * x, n // 2)

            return res if not n % 2 else res * x
        output = recurse(x, abs(n))
        return output if n > 0 else (1/output)