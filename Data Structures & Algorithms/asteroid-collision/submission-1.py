class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Input: asteroids = [2,4,-4,-1]
        Output: [2]

        We need to keep values in a stack. 
        
        while stack and their is a collision: 0 < stack[-1] < asteroids[i]

        """
        stack = []

        for a in asteroids:
            # collision found
            while stack and a < 0 < stack[-1]:
                # stack[-1] is larger if diff is pos
                # a is larger if diff is neg
                diff = abs(stack[-1]) - abs(a)

                # is a is larger then keep popping
                if diff < 0:
                    stack.pop()
                    continue
                elif diff == 0:
                    stack.pop()
                # stack.append(a)
                break
            else:
                stack.append(a)
        return stack

        