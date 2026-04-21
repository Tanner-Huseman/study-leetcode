from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Monotonic stack over nums2. Pre-build value→index map for nums1 so lookup is O(1).
        Stack holds indices of nums2 in decreasing value order (waiting room).
        When a greater element arrives, pop and record answers for any nums1 elements.

        Time: O(n + m) — n=len(nums2), m=len(nums1)
        Space: O(n + m)
        """
        nums1_map = {v: i for i, v in enumerate(nums1)}
        stack = []
        result = [-1] * len(nums1)

        for i, num in enumerate(nums2):
            while stack and nums2[stack[-1]] < num:
                idx = stack.pop()
                ri = nums1_map.get(nums2[idx])
                if ri is not None:       # can't use `if ri` — index 0 is falsy
                    result[ri] = num
            stack.append(i)

        return result
