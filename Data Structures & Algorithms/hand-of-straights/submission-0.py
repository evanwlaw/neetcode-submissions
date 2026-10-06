import heapq
class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        """
        Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4
        Output: true

        freq map of value : count
        1 : 1
        2 : 2
        3 : 2
        4 : 2
        5 : 1

        and minheap of the keys (cards)

        1   2   3   4   5

        iterate through heap:
            first card = heaptop

            then from first card to first + groupSize:
                see if card is in heap
                decrement when we see it 
                if card is not in heap, then return false
                if card in map has 0 or less, then it's also invalid because means we ran out of cards for valid

        hand needs to be divisible by groupsize
        """
        if len(hand) % groupSize:
            return False

        cardCounts = {}
        for card in hand:
            cardCounts[card] = 1 + cardCounts.get(card, 0)

        cardHeap = list(cardCounts.keys())
        heapq.heapify(cardHeap)

        while cardHeap:
            first = cardHeap[0]

            for i in range(first, first + groupSize):
                if i not in cardCounts or cardCounts[i] <= 0:
                    return False
                cardCounts[i] -= 1
                if cardCounts[i] == 0:
                    heapq.heappop(cardHeap)
        return True
