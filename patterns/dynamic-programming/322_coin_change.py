from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = fewest coins to make amount i
        # float('inf') = unreachable until proven otherwise
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # base case: 0 coins to make amount 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]
