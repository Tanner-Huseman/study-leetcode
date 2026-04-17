from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)  # lo=1: can't eat 0 bananas/hour

        while lo < hi:
            mid = (lo + hi) // 2
            if self.isFeasible(mid, piles, h):
                hi = mid       # mid works — try slower
            else:
                lo = mid + 1   # too slow — must go faster

        return lo  # lo == hi == minimum feasible speed

    def isFeasible(self, k: int, piles: List[int], h: int) -> bool:
        return sum(ceil(p / k) for p in piles) <= h
