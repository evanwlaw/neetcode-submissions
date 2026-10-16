class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """

        if t[i] > target[i] -> out
        if t[i] == target[i] -> append to check
        if len(check) == len(target) -> True
        """

        check = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            for i in range(3):
                if t[i] == target[i]:
                    check.add(i)
        return len(check) == 3