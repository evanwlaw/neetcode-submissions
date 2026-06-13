class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        9
        1   4   3   2
        
        if rate = 1
        1   4   3   2   -> 10 hrs
        
        if rate = 2
        1   2   2   1   -> 6 hrs

        if rate = 3
        1   2   1   1   -> 5 hrs

        if rate = 4
        1   1   1   1   -> 4

    
        binary search on the rate from 1 to max(piles)

            while rate is smaller than max num of bananas:
                
                for each pile, get the time
                    time per pile = pile[i] // rate -> round up
                
                if total time of piles with this rate <= h:
                    see if this rate k is smaller than the min k seen so far
                else, we've gone over and need to increase rate k

            

        """

        l = 1
        r = max(piles)
        min_k = r

        while l <= r:
            k = (l + r) // 2
            time = 0

            for p in piles:
                time += math.ceil(p / k)
            
            if time <= h:
                min_k = min(min_k, k)
                r = k - 1
            else:
                l = k + 1
            
        return min_k



