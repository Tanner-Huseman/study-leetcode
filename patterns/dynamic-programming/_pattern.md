<!-- STATUS: complete -->
# Dynamic Programming (1D)

## The Concept
Solves problems where the answer at position `i` depends on answers at earlier positions. Store subproblem results in a `dp` array to avoid recomputing overlapping work. Core discipline: define what `dp[i]` means in plain English *before* writing the recurrence — get that wrong and nothing else works.

## The Template
```python
def dp_1d(nums):
    n = len(nums)
    dp = [0] * n          # dp[i] = answer to subproblem ending at/up to index i
    dp[0] = nums[0]       # base case: seed manually

    for i in range(1, n):
        # recurrence: express dp[i] in terms of dp[i-1], dp[i-2], etc.
        dp[i] = max(dp[i-1], some_function(dp[i-2], nums[i]))

    return dp[n-1]         # or max(dp) — depends on whether answer is always at the end
```

## When to Recognize It
- "Maximum/minimum/count of ways" over a sequence
- Decision at each step: take it or skip it
- Brute force has exponential branching — same subproblems recur
- "How many ways...", "minimum cost...", "longest subsequence/subarray..."
- Problem has **optimal substructure**: best solution contains best sub-solutions

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|------------|-------------|
| 198 | House Robber | Medium | `dp[i] = max(nums[i] + dp[i-2], dp[i-1])`; `dp[i-1]` carries full optimal history forward — no need to track which houses were robbed |
| 322 | Coin Change | Medium | `dp[i] = min(dp[i], dp[i-c] + 1)` for each coin; initialize with `float('inf')` (unreachable), `dp[0] = 0` (base case) |

## Gotchas / Failure Modes
- **Wrong `dp[i]` definition**: the most common mistake — "amount robbed so far" is ambiguous; be precise: "maximum robbable from houses 0 through i".
- **`dp[i-2]` out of bounds**: guard with `if i-2 >= 0 else 0` (or seed `dp[1]` separately and start loop at 2).
- **Returning `dp[n-1]` vs `max(dp)`**: if the optimal answer isn't always at the last index (e.g., longest increasing subsequence), return `max(dp)`.
- **Space optimization**: the full `dp` array is O(n) but most 1D problems only need the last 1-2 values — replace with two variables (`prev2, prev1`) for O(1) space once the recurrence is understood.
- **Not the right pattern**: if the decision at `i` depends on a *range* of earlier values (not just `i-1`, `i-2`), you may need 2D DP or a different approach.
- **`float('inf')` for minimization**: use `float('inf')` as the default when you're minimizing and a subproblem may be unreachable. `inf + 1 == inf` so the math stays safe even without an explicit guard. Check `== float('inf')` at the end to detect impossible cases.
- **dp array size**: for amount-based problems, `dp` is size `amount + 1` (indices 0 through `amount`), not `len(coins)`.
