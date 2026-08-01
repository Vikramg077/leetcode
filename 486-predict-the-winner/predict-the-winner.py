from typing import List

class Solution:
    def predictTheWinner(self, scores: List[int]) -> bool:
        length = len(scores)

        # If the number of elements is even,
        # Player 1 can always secure a win.
        if length % 2 == 0:
            return True

        # DP array to store score differences
        bestDiff = scores[:]

        for left in range(length - 2, -1, -1):
            for right in range(left + 1, length):
                pickLeft = scores[left] - bestDiff[right]
                pickRight = scores[right] - bestDiff[right - 1]
                bestDiff[right] = max(pickLeft, pickRight)

        return bestDiff[-1] >= 0