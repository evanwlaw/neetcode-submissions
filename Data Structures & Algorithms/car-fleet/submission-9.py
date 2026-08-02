class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
        Output: 3

        0   1   2   3   4   5   6   7   8   9   10
                        2
            2
        1                           
                                    1
        Time to target = (target - position) / speed 
        1st -> 6 / 2 = 3
        2nd -> 9 / 2 = 4.5
        3rd -> 10/ 1 = 10
        4th -> 3 / 1 = 3

        Slowest car would force other cars into fleet (can't pass)

        [7, 1] -> 3
        [4, 2] -> 3
        [1, 2] -> 4.5
        [0, 1] -> 10


        if stack[-1] => stack[-2]:
            stack.pop()
        """

        check = []
        n = len(position)
        for i in range(n):
            check.append([position[i], speed[i]])
        
        stack = []

        for pos, spd in sorted(check)[::-1]:
            stack.append((target - pos) / spd)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
