class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Input: 
        gas = [1,2,3,4], 
        cost = [2,2,4,1]
        Output: 3

        gas = [1,   2,  3,  4], 
       cost = [2,   2,  4,  1]
       diff = [-1   0   -1  3]
       if there is a sol, then there is at more one solution

        from the diff, we see that we can only go through gas stations i = 1 or i = 3 to get to the next station. however if starting from i = 1, we find that we can't contninue on to the station after.

        and in general, we the sum of gas needs to be >= to sum of cost to have a soluton


        gas = [1,   2,   3,   4,   5]
       cost = [3,   4    5    1    2]
       diff = [-2   -2  -2    3    3]
        """
        # invalid, no solution if cost is more than the gas provided
        if sum(gas) < sum(cost):
            return -1

        output = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                output = i + 1
                total = 0
        return output

                
