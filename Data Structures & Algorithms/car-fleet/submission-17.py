class Solution:
     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
          """
          Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
          Output: 3
          
     pos       0    1    2    3    4    5    6    7    8    9    10
     speed                         2 
                    2
               1
                                                  1

          Carfleets -> need to find time to target of each car -> (target - pos)/speed
          pos, speed
          4, 2 -> 10 - 4 / 2 -> 3
          1, 2 -> 10 - 1 / 2 -> 4.5
          0, 1 -> 10 - 0 / 1 -> 10
          7, 1 -> 10 - 7 / 1 -> 3

          We see that cars of same time to target will create the same car fleet -> [4,2] + [7,1]

          We need to combine both arrays into a single array where each value is -> [pos,speed]

          Can we iterate through this new array to get the number of fleets?
               - At each iteration through this new array,
                    Calulate time to target -> if we continue, we lose access to this time to target.
                    We do need to keep the ones in it that take longer and expel ones that are equal/smaller than the one we're checking (if the one we're checking has a smaller time to target, then this car will be th one that holds everything up)

          We can sort the new array by position -> use a monotonic stack to keep time to target as values.
          Push to stack each time to target that we calculated -> pop while stack[-1] >= stack[-2]

          Time Complexity: O(NlogN) - Zipping up the two arrays will take O(N) time. Sorting algorithm will take O(NlogN) time. Iterating through the new array will take O(N) time as well. So final complexity is O(NlogN) as the sort dominates the time complexity
          Space Complexity: O(N) - Extra space is used to hold the new array with N values. And a stack is kept to hold the car fleets. Worst case is that each car is a unique car fleet by itself. Final space complexity is O(N)
          
          """
          stack = []
          carInfo = []
          # zip array
          for pos, speed in zip(position, speed):
               carInfo.append([pos,speed])

          # sort in desc order of position
          carInfo.sort()

          # iterate through carinfo and find car fleets
          for pos, speed in carInfo[::-1]:
               stack.append((target - pos) / speed)

               while len(stack) >= 2 and stack[-1] <= stack[-2]:
                    stack.pop()
          return len(stack)

