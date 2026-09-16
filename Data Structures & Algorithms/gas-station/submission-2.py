class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Input: gas = [1,2,3,4], cost = [2,2,4,1]
        Output: 3


        gas = [1,2,3,4]
        cos = [2,2,4,1]

        Starting from station 3:
        tank = 4

        from station 3 to 0:
            tank = tank - cost[3] + gas[0] = 4 - 1 + 1 = 4
        
        from station 0 to 1:
            tank = tank - cost[0] + gas[1] = 4 - 2 + 2 = 4

        from station 1 to 2:
            tank = tank - cost[1] + gas[2] = 4 - 2 + 3 = 5
        
        fromt station 2 to 3:
            tank = tank - cost[2] = 5 - 4 = 4

        Cannot start from 0,1,2 because the gas at those stations is not enough to go to next one:
        Greedily, we notice that we can only start on that station if gas[i] >= cost[i] 


        gas  [1,2,3,4]
        cost [2,2,4,1]
        diff [-1, 0, -1, 3]

        There is only one solution at most. And there is a solution if sum(gas) >= sum(cost)
        We could start at gas[1] but we wouldnt be able to complete a circle that gas[3] allows us to.
        We can then see at the valid i, we see the diff combined before that has to be smaller, and after the valid i everything would allow us to cycle entire thing zonce (if we start i more then we would be short).

        If our current total ever dips below 0, we know the idx we're looking at is wrong:
            reset idx to idx + 1
            total = 0

        
        """

        if sum(gas) < sum(cost):
            return -1 # no solution

        output, total = 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                output = i + 1
                total = 0
        return output
