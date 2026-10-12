class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        Input: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]
        Output: false
        
        triplets[0] -> 2   5   6
        triplets[1] -> 1   4   4
        becomes -> 2    5   6

        prevmerged  -> 2    5   6
        triplets[2] -> 5    5   5
        becomes -> 5    5   6

        we need to track what's the merged triplet so far
            - seed with triplet[0]
        
        if merged[i] > target[i] -> we know this cant be valid so return False immediately

        """

        # merged = triplets[0]

        # for t in triplets:
        #     for i in range(len(t)):
        #         # update merged
        #         merged[i] = max(merged[i], t[i])
        #         if merged[i] > target[i]:
        #             return False


        # return True

        """
        looks like we just need to find any two that can be merged

        we can elimnate triplets with values that are larger than ones in target...we can just skip them

        if they're smaller, let's see if any them == target

        """
        good = set()

        for t in triplets:
            
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3

