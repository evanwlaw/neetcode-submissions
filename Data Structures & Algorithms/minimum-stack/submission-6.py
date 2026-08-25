class MinStack:
    """
    init
    push 1
    push 2
    push 0
    getMin -> 0
    pop -> pop 0
    top -> 2
    getMin -> 1


    if we push 1 to stack, we know it's the current min in stack. 
    stack
    1

    if we push 2 to the stack, we lose the a way to know if the 1 is the min of the stack. we just see the stack top as 2
    stack
    2
    1

    if we push 0 to the stack, we lose the a way to know if this current pushed value is the new min or not. we just see the stack top as 0
    stack
    0
    2
    1

    if we pop from stack, we lose are supposed to lose the 0 as min but dont have the abiliyt to see the next min (at the bottom of the stack)
    stack
    2
    1



    we use two stacks: stack and minStack. 
    stack holds the values we push/pop. while minStack pushes the min value to it compared with the last one in stack, this holds as we push to stack from nothing so we push the same on into minvalue. next pushed to stack and see if the new value < minstack[-1] -> update accordingly

    stack   minStack
    1       1

    push 2
    stack   minStack
    0       0
    2       1
    1       1

    further optimization is to use one stack and a tuple
    """
    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
        
    #     if self.minStack and self.minStack[-1] < val:
    #         self.minStack.append(self.minStack[-1])
    #     else:
    #         self.minStack.append(val)

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minStack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minStack[-1]


    def __init__(self):
        self.stack = []
        # self.minStack = []

    def push(self, val: int) -> None:
        if self.stack and self.stack[-1][1] < val:
            self.stack.append([val, self.stack[-1][1]])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
    
    """
    [4,0]
    [2,0]
    [0,0]
    [5,5]

    """
