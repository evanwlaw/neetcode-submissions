class Solution:
     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
          """
          Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
          Output: 3

          pos     0    1    2    3    4    5    6    7    8    9    10
          speed                       2
                       2
                  1
                                                     1

          Time to target = (target - position) / speed
          pos = 4, speed 2 -> T2T = 10 - 4 / 2 -> 3
          pos = 1, speed 2 -> T2T = 10 - 1 / 2 -> 4.5
          pos = 0, speed 1 -> T2T = 10 - 0 / 2 -> 5
          pos = 7, speed 1 -> T2T = 10 - 7 / 2 -> 3
          
          From this, we see pos 4 and pos 7 cars will catch up to each other -> fleet

          We need some way to hold the cars in a datastructure where most recent car takes longer time to target than before.

          A stack is perfect for this.
          - Each value in stack is the time to target. (we need to sort cars by position, in desc)
          - The stack values need to be monotonically increasing
          - pop from stack while current speed is smaller than top of stack

          
          """
          carInfo = []

          for pos, speed in zip(position, speed):
               carInfo.append([pos,speed])

          carInfo.sort(reverse=True)

          stack = []

          for pos, speed in carInfo:
               stack.append((target-pos)/speed)
               while len(stack) >= 2 and stack[-1] <= stack[-2]:
                    stack.pop()
          return len(stack)