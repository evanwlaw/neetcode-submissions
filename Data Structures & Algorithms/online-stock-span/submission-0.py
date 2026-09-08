class StockSpanner:
    """
    75,1

    60, 1
    70, 2
    80, 1
    100, 1

    while price >= stack[-1],
        span += stack[-1][1]
        stack.pop()
    """
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])
        return self.stack[-1][1]
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)