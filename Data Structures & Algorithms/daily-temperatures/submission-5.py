class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Input: temperatures = [30,38,30,36,35,40,28]
                    Output:   [1, 4,  1, 2, 1, 0, 0]

        we need keep idxes until they're processed. Meaning we're able to find the num of days there is warmer day

        stack (indices):
        i = 0 

        """
        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                output[idx] = i - idx
            stack.append(i)

        return output