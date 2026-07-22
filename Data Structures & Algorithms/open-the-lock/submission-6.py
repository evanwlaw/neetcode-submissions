class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        if target in deadends or "0000" in deadends:
            return -1

        side1 = set(["0000"])
        side2 = set([target])
        visited = set(deadends)
        steps = 0

        while side1 and side2:
            # swap "sides" if one frontier is smaller
            if len(side1) > len(side2):
                side1, side2 = side2, side1
            steps += 1
            nextFrontier = set()

            for value in side1:
                # generate next neighbors
                for i in range(4):
                    for diff in (-1, 1):
                        newdigit = str((int(value[i]) + diff) % 10)
                        nextValue = value[:i] + newdigit + value[i + 1:]
                        # overlap w/ opposide side, then it means both sides met, return steps
                        if nextValue in side2:
                            return steps
                        if nextValue in visited: # skip if visited
                            continue
                        visited.add(nextValue)
                        nextFrontier.add(nextValue)
            side1 = nextFrontier
        return -1