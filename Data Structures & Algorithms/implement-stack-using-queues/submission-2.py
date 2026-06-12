class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)
        
    def pop(self) -> int:
        """
        keep popping from q1 until before last one (e.g. 4)
        as we pop, enque to q2
        then
        q1 = 1   2   3   4
        q2 = 
        """
        n = len(self.q1)
        for i in range(n - 1):
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()

        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        return self.q1[-1]        

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()