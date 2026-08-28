class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Input: piles = [1,4,3,2], h = 9
        Output: 2

        piles[i] -> # of bananas in pile
        h -> time given to eat all

        Output is k -> min rate of banans per hour to eat all piles within h

        go through piles:
            at pile[i] -> we know current # of banana in pile. we don't know the min rate k it takes to eat this current pile. 
            
            we need to figure out the rate (k)


            if k == 1 -> piles[0] takes 1 hr
                         piles[1] takes 4 hr
                         piles[2] takes 3 hrs
                         piles[3] takes 2 hrs
                         total ->10 hrs, invalid
            if k == 2 -> piles[0] takes 1 hr bc has to be whole
                         piles[1] takes 2 hr
                         piles[2] takes 2 hrs
                         piles[3] takes 1 hrs
                         total -> 6 hrs, valid

            if k == 3 -> piles[0] takes 1 hr bc has to be whole
                         piles[1] takes 2 hr
                         piles[2] takes 1 hrs
                         piles[3] takes 1 hrs
                         total -> 5 hrs, valid

            if k == 4 -> piles[0] takes 1 hr bc has to be whole
                         piles[1] takes 1 hr
                         piles[2] takes 1 hrs
                         piles[3] takes 1 hrs
                         total -> 4 hrs, valid

            As k rate increases, the number hrs decreases. The max value of all piles can be our upper bound. 
            As k rate decreases, the number hrs decreases. Our lower bound is when the total is more than h

        general algorithm:
            binary search of rates of k (range from 1 : max(piles))
                iterate through all piles to get total hrs with current rate.
        Time Complexity: O(N * log M) - The binary search is O(log M) time but for each search where m is the max number of bananas in all piles. We have to iterate through all the piles which is O(N) time. Final time complexity is O(N * log M)
        Space Complexity: O(1) - Extra space is used to hold variables of our binary search window and k/output.
        Time Spent on problem: 25m 
        """
        k = float("inf")
        l, r = 1, max(piles)
        
        while l <= r:
            middle = (l + r) // 2 
            hours_curr_rate = 0
            
            for b in piles:
                hours_curr_rate += math.ceil(b/middle)
            if hours_curr_rate > h:
                l = middle + 1
            else:
                k = min(k, middle)
                r = middle - 1
        
        return k