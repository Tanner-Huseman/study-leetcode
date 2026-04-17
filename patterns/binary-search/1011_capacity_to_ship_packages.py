from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # lo = max(weights): ship must fit the heaviest single package
        # hi = sum(weights): ship everything in one day
        lo, hi = max(weights), sum(weights)

        while lo < hi:
            mid = (lo + hi) // 2
            if self.isFeasible(mid, weights, days):
                hi = mid       # mid works — try smaller capacity
            else:
                lo = mid + 1   # too small — need more capacity

        return lo

    def isFeasible(self, wc: int, weights: List[int], days: int) -> bool:
        day_count = 1
        remaining_capacity = wc
        for w in weights:
            remaining_capacity -= w
            if remaining_capacity < 0:  # package doesn't fit today — start new day
                day_count += 1
                remaining_capacity = wc - w
        return day_count <= days
