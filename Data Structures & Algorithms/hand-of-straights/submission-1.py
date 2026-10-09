class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4
        Output: true
        Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].


        to even have hand split up, check if len(hand) % groupSize -> if not 0, then false

        use a freqMap to see how many of each card we have
        1 : 1
        2 : 2
        3 : 2
        4 : 2
        5 : 1

        use minHeap on the card values to get next card

        minHeap = 1 2 3 4 5

        iterate through minHeap
            get smallest minHeap[0] for first card

            from first to first + groupSize:
                return false if not in heap or card freq is 0
                
                otherwise decrement

        """

        if len(hand) % groupSize:
            return False

        freqMap = {} # cardnumber : freq count

        for card in hand:
            freqMap[card] = 1 + freqMap.get(card, 0)

        minHeap = list(freqMap.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for card in range(first, first + groupSize):
                if card not in minHeap or freqMap[card] <= 0:
                    return False
                freqMap[card] -= 1
                if freqMap[card] == 0:
                    heapq.heappop(minHeap)
        return True