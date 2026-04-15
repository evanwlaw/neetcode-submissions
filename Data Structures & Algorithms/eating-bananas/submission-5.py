class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k -> rate of bananas per hour
        h -> hours given

        binary search the rate k. From 1 to max(piles).
        k = (l + r) // 2

        then for each p in piles, see total hrs with rate k
        
        if hours <= h:
            res = min(res, k)
            r = k - 1

        """

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
