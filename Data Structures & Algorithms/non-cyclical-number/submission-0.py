class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSq(n)

        while slow != fast:
            fast = self.sumSq(fast)
            fast = self.sumSq(fast)
            slow = self.sumSq(slow)
        return True if fast == 1 else False


    def sumSq(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output