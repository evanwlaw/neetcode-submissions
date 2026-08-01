class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []

        sort_pos = []
        for i in range(n):
            sort_pos.append([position[i], speed[i]])

        sort_pos.sort(reverse=True)

        for pos, spd in sort_pos:
            # if stack and position[i] < stack[-1][0] and stack[-1][1] >= speed[i]:
            #     continue

            time = (target - pos) / spd
            stack.append(time)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)