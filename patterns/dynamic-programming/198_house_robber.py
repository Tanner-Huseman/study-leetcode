from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]  # base case: only one house, rob it

        for i in range(1, n):
            # two choices at each house:
            # 1. rob it: nums[i] + best up to i-2 (skip i-1 to avoid alarm)
            # 2. skip it: best up to i-1
            last_house_val = dp[i-2] if i-2 >= 0 else 0
            dp[i] = max(nums[i] + last_house_val, dp[i-1])

        return dp[n-1]
