import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        figure out if we can rearrange our hand into consec increasing hand

        if hand is not divisiable by groupSize, then we cant return anything valid

        Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4
        Output: true

        1 : 1
        2 : 2
        3 : 2
        4 : 2
        5 : 1

        need to track how many of each card we have -> map

        iterate through the set of the cards we have:
            if n - 1 not in set -> first card in group size
                for i in range(first card : first card + groupSize):
                    if i not in set or map[i] == 0:
                        return False

        """
        # if len(hand) % groupSize: # if this is false, then it is divisible
        #     return False
        
        # freq = {} # card num : freq

        # for n in hand:
        #     freq[n] = 1 + freq.get(n, 0)
        
        # handSet = set(freq.keys())

        # for card in handSet:
        #     if card - 1 not in handSet: # first card found
        #         first = card

        #         for i in range(first, first + groupSize):

        #             if i not in handSet or freq[i] <= 0:
        #                 return False
        #             freq[i] -= 1
        # return True

        """
        close -> but instead of a set, use a minheap to get the smallest card.
        """
        if len(hand) % groupSize: # if this is false, then it is divisible
            return False
        
        freq = {} # card num : freq

        for n in hand:
            freq[n] = 1 + freq.get(n, 0)
        
        minHeap = list(freq.keys())
        heapq.heapify(minHeap)

        while minHeap:
            firstCard = minHeap[0]

            for card in range(firstCard, firstCard + groupSize):
                if card not in minHeap or freq[card] <= 0:
                    return False
                freq[card] -= 1
                if freq[card] == 0:
                    heapq.heappop(minHeap)
        return True

