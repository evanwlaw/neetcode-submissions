class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        positive ->
        negative <-

        if pos and neg then collide:
            - smaller explodes
            - or if same size both explode
        
        Input: asteroids = [2,4,-4,-1]
        Output: [2]

        i = 0
        nothing

        i = 1
        nothing because both pos

        i = 2
        it hits previous 4 and both explode because they're the same.

        i = 3
        -1 and 2 hit each other but -1 explodes bc smaller in abs


        a stack will be a good structure to use as we need to keep unexploded asteroids until "processed".
        stack[i] = the value of the unexploded asteroid (dont need to hold idx bc we dont need to track placement)

        collision only when top of stack is positive and next asteroid is negative




        push when stack is empty
        while stack and asteroid[i] < 0 < stack[-1]:
            if abs(stack[-1]) < asteroid[i] -> pop stack
        stack.append(asteroid[i])

        [2,4, -4, -1, 3, -5]

        when i = 5
        stack:
        3
        2
        need to pop all and push -5
        """

        stack = []

        for i in range(len(asteroids)):
            #collision
            while stack and asteroids[i] < 0 < stack[-1]:
                if abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                    continue
                elif abs(stack[-1]) == abs(asteroids[i]):
                    # both explode
                    stack.pop()
                break
    
            else:    
                stack.append(asteroids[i])
                    
        return stack
