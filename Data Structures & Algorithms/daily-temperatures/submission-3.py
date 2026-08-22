class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input: temperatures = [30,38,30,36,35,40,28]
        Output: [1,4,1,2,1,0,0] 


        output is an array where output[i] holds the value of how many "days" or the len of how many days before a larger temp

        iterate through temperatures

        temperatures[0] -> 30
        if we continue, we lose the ability to track this (e.g if next one is higher/lower than curr). we need to keep holding 30 until we see somethin
        output = [0,0,0,0,0,0,0]

        temperatures[1] -> 38
        if we continue, we lose the ability to track this and we wouldnt that it was larger than temperatures[0], so that output[0] becomes 1. and we need to keep holding the 38 until we see a higher one
        output = [1,0,0,0,0,0,0]

        temperatures[2] -> 30
        if we continue, we lose the ability to track this. and we need to keep holding the 30 until we see a higher one
        output = [1,0,0,0,0,0,0]

        temperatures[3] -> 36
        if we continue, we lose the ability to track this. and we need to keep holding the 36 until we see a higher one. the previous 30 at temperatures[2] is solved so output[2] becomes 1
        output = [1,0,1,0,0,0,0]

        temperatures[4] -> 35
        if we continue, we lose the ability to track this. and we need to keep holding the 35 until we see a higher one. 
        output = [1,0,1,0,0,0,0]

        temperatures[5] -> 40
        if we continue, we lose the ability to track this. and we need to keep holding the 40 until we see a higher one.
            the previous 35 at temperatures[4] is solved so output[4] becomes 1
            the previous 36 at temperatures[3] is solved so output[3] becomes 2
            the previous 40 at temperatures[1] is solved so output[2] becomes 4
        output = [1,4,1,2,1,0,0]

        temperatures[6] -> 28
        if we continue, we lose the ability to track this. and we need to keep holding the 28 until we see a higher one.
        output = [1,4,1,2,1,0,0]

        so we need to track the where we are in temperatures, index?
        And using a stack would be most helpful for this. Each value of stack is the index of the tempearture we're holding until we see something higher.

        Keep holding in until temperatures[top of stack] < temperatures[i]. and keep popping from stack while that is true. 
            from the idx popped from stack -> output[top of stack] = i - popped idx from stack for num of days.

        For each iteration, the stack holds indexes of temperatures that are smaller than where we are at (temperatures[i])

        """

        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = i - idx
            else:
                stack.append(i)
        return output