class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Input: asteroids = [2,4,-4,-1]
        Output: [2]

        We need to keep values in a stack. 
        
        while stack and their is a collision: 0 < stack[-1] < asteroids[i]
        1. pop
        2. 
        """
        stack = []
        
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if abs(a) > abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(a) == abs(stack[-1]):
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack