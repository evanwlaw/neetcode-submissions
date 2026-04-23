class MinStack:
    """
    0   0
    2   1
    1   1

    [0,0]
    [2,1]
    [1,1]
    """

    def __init__(self):
        self.minStack = []
        

    def push(self, val: int) -> None:
        if self.minStack:
            self.minStack.append([val, min(val, self.minStack[-1][1])])
        else:
            self.minStack.append([val, val])


    def pop(self) -> None:
        del self.minStack[-1]
        

    def top(self) -> int:
        return self.minStack[-1][0]
        

    def getMin(self) -> int:
        return self.minStack[-1][1]

        
