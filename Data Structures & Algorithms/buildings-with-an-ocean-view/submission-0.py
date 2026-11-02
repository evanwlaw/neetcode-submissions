class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        return list of indices where the building height[i] can see ocean.
        a height[i] can see ocean if buildings to right are strictly shorter.


        Input: heights = [4,2,3,2,1]
        Output: [0,2,3,4]

        0   1   2   3   4
        4   2   3   2   1
        O   x   O   O   O

        Input: heights = [1,3,2,4,2,5,1]
        Output: [5,6]

        0   1   2   3   4   5   6
        1   3   2   4   2   5   1
        O   X   X   X   X   O   O

        Seems we need to keep possible idx's in a structure while iterating.

        stack -> stack[i] is index of a building that is have an ocean view. Strictly descreasing order (monotonic stack)

        while stack and heights[stack[-1]] <= heights[i] -> pop from stack
        """
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack
