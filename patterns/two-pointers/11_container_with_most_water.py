from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_volume = 0

        while l < r:
            lh = height[l]
            rh = height[r]
            width = r - l
            max_volume = max(max_volume, min(lh, rh) * width)

            # always move the shorter wall — moving the taller one
            # can only decrease height while also decreasing width
            if lh > rh:
                r -= 1
            else:
                l += 1

        return max_volume
