from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Sort, fix one element in outer loop, two pointers on remainder.
        Track closest sum by comparing abs(diff) at each triplet.

        Time: O(n^2)
        Space: O(1) excluding sort
        """
        closestSum = nums[0] + nums[1] + nums[2]  # real init, not inf
        nums.sort()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                diff = target - (nums[i] + nums[j] + nums[k])
                if abs(diff) < abs(target - closestSum):
                    closestSum = nums[i] + nums[j] + nums[k]
                if diff < 0:
                    k -= 1
                else:
                    j += 1
        return closestSum
