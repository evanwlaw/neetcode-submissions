class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}

        l, total, res = 0, 0, 0

        for r in range(len(fruits)):
            count[fruits[r]] = 1 + count.get(fruits[r], 0)
            # total += 1

            # current window has 3+ types 
            while len(count) > 2:
                count[fruits[l]] -= 1
                # total -= 1
                if not count[fruits[l]]: # pop if 0
                    count.pop(fruits[l])
                l += 1 # make window smaller

            res = max(res, r - l + 1)
        return res