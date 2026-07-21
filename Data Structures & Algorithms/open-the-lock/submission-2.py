class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        output = 0
        visited = set(deadends)

        if "0000" in visited:
            return -1

        while queue:
            for _ in range(len(queue)):
                value = queue.popleft()

                if value == target:
                    return output
                # if value not in visited:
                #     visited.add(value)

                for i in range(4):
                    for diff in (-1, 1):
                        newdigit = str((int(value[i]) + diff) % 10)
                        check = value[:i] + newdigit + value[i + 1:]
                        if check not in visited:
                            queue.append(check)
                            visited.add(check)
            output += 1

        return -1