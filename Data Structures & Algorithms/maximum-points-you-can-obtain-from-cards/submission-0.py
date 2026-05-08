class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        max_sum of cards = total sum - unpicked cards -> min sum of unpicked gets us max sum of picked

        """
        total = sum(cardPoints)
        if k == len(cardPoints): return total

        card_sum = 0
        max_points = 0
        l = 0

        for r in range(len(cardPoints)):
            card_sum += cardPoints[r]

            if r - l + 1 == len(cardPoints) - k:
                max_points = max(total - card_sum, max_points)
                card_sum -= cardPoints[l]
                l += 1

        return max_points