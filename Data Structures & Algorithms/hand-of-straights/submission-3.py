import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        so end goal is to figure out if the hand hand we have is able to be rearranged into consec groups of size groupSize -> return bool

        if hand isnt divisible by groupSize -> impossible to have valid hand

        in the hand, there could be dupes and unsorted 

        Input: hand = [1,2,4,2,3,5,3,4], groupSize = 4
        Output: true
        Explanation: The cards can be rearranged as [1,2,3,4] and [2,3,4,5].


        Need to track how many of each -> hashmap
        1 : 1
        2 : 2
        3 : 2
        4 : 2
        5 : 5

        we need to start from start/min of hand to see if we have consecs.
        use a minHeap of the unique cards we have in map (keys)

        so minheap: 1 2 3 4 5

        go through heap
            top of heap is the card we checking

            from the val of this card to card.val + groupSize:
                make sure each card is valid: in heap and val > 0

                if card is not heap or it's val in map is <= 0, 
                    it's invalid. 

                else:
                    decrement by 1
                    if val in map == 0 -> pop from minheap
        
        trace:
            check cards 1-4
                check 1 -> in minheap and val > 0 -> decrement to 1:0 and pop from min heap
                check 2 -> in minheap and val > 0 -> decrement to 2:1
                check 3 -> in minHeap and val > 0 -> decrement to 3:1
                check 4 -> in minHeap and val > 0 -> decrement to 4:1
            in minHeap = 2  3   4   5

            check cards 2-5
                check 2 -> in minheap and val > 0 -> decrement to 2:0 and pop from min heap
                check 3 -> in minheap and val > 0 -> decrement to 3:0 and pop from min heap
                check 4 -> in minheap and val > 0 -> decrement to 4:0 and pop from min heap
                check 5 -> in minheap and val > 0 -> decrement to 5:0 and pop from min heap
            return True

        Input: hand = [1,2,3,3,4,5,6,7], groupSize = 4
        map
        1 : 1
        2 : 1
        3 : 2
        4 : 1
        5 : 1
        6 : 1
        7 : 1

            check cards 1-4
                check 1 -> in minheap and val > 0 -> decrement to 1:0 and pop from min heap
                check 2 -> in minheap and val > 0 -> decrement to 2:0 and pop from min heap
                check 3 -> in minHeap and val > 0 -> decrement to 3:1
                check 4 -> in minHeap and val > 0 -> decrement to 4:0 and pop from min heap
            in minHeap = 3  5   6   7
            check cards 3-7
                check 3 -> in minHeap and val > 0 -> decrement to 3:0 and pop from min heap
                check 4 -> NOT in minHeap and val == 0 -> invalid, return False
        """

        if len(hand) % groupSize: # if true then means we have non 0 value, invalid
            return False

        cardFreq = {} # val : freq
        for card in hand:
            cardFreq[card] = 1 + cardFreq.get(card, 0)
        
        minHeap = list(cardFreq.keys())
        heapq.heapify(minHeap)

        while minHeap:
            card = minHeap[0]

            for c in range(card, card + groupSize):
                if c not in minHeap or cardFreq[c] <= 0:
                    return False
                else:
                    cardFreq[c] -= 1
                    if cardFreq[c] == 0:
                        heapq.heappop(minHeap)

        return True
        