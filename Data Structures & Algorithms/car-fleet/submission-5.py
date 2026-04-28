class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

        Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

        sorted array in desc order of pos -> [pos, speed]

        pos 7   4   1   0
        spe 1   2   2   1
        tim 3   3   4   10
        
        time to target = (target - position)/ speed


        stack -> [time,time2]

        pop if stack[-1] <= stack[-2]

        return len(stack)
        
        """
        check = []
        for i in range(len(position)):
            check.append([position[i], speed[i]])
        stack = []
        for p, s in sorted(check)[::-1]:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
