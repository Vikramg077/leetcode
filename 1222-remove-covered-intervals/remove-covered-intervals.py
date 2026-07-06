from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by starting point, and if equal, by decreasing ending point
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))

        visible_intervals = 0
        farthest_end = float("-inf")

        for start, finish in intervals:
            if finish > farthest_end:
                visible_intervals += 1
                farthest_end = finish

        return visible_intervals