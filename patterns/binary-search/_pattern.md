<!-- STATUS: complete -->
# Binary Search (on Answer)

## The Concept
Instead of searching an array for a value, search the **space of possible answers** for the optimal one. If you can write a greedy feasibility check ("is answer X achievable?"), binary search finds the boundary between feasible and infeasible in O(log(range)) iterations.

## The Template
```python
def binary_search_on_answer(nums):
    lo, hi = min_possible_answer, max_possible_answer

    while lo < hi:
        mid = (lo + hi) // 2

        if feasible(mid, nums):   # can we achieve 'mid'?
            hi = mid              # mid works — try smaller (minimization)
        else:
            lo = mid + 1          # mid doesn't work — need larger

    return lo  # lo == hi == smallest feasible value


def feasible(candidate, nums) -> bool:
    # greedily verify: is 'candidate' achievable?
    # typically an O(n) scan
    ...
```

> **Maximization** (largest value that works): use `lo = mid` when feasible, `hi = mid - 1` when not, and `mid = (lo + hi + 1) // 2` to avoid infinite loop.

## Why Binary Search Works Here (Monotonicity)

The answer space is **monotonic**: if speed `k` is feasible, then `k+1` is also feasible (faster is always at least as good). If `k` is not feasible, neither is `k-1`. This creates a clean threshold — all values below it fail, all values above it pass — and binary search finds that exact boundary in O(log n) instead of scanning every value linearly.

**Diagnostic question**: before using this pattern, ask yourself — *"Is there a threshold where below it always fails and above it always succeeds?"* If yes, binary search on the answer.

## Python Syntax Notes

```python
from math import ceil
ceil(7 / 3)      # → 3  (rounds up to nearest integer)
ceil(6 / 3)      # → 2  (exact division, no rounding)

7 // 3           # → 2  (floor division — rounds DOWN, integer result)
(7 + 3 - 1) // 3 # → 3  (integer ceiling without importing math: (n + d - 1) // d)
```

`//` is floor division — always rounds toward negative infinity and returns an int. Useful to avoid floats entirely in binary search problems.

## When to Recognize It
- "Minimize the maximum" or "maximize the minimum" phrasing
- The answer is a number within an obvious range
- Given a candidate answer, you can verify it greedily in O(n)
- Brute-forcing every possible answer would be too slow
- Keywords: "split into k pieces", "ship within D days", "minimum speed", "allocate"

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|------------|-------------|
| 875 | Koko Eating Bananas | Medium | Search `[1, max(piles)]`; feasible = `sum(ceil(p/k)) <= h` |

## Gotchas / Failure Modes
- **lo = 0 instead of 1**: if the candidate is used as a divisor (like eating speed), 0 causes a ZeroDivisionError — always set lo to the true minimum meaningful value.
- **Wrong convergence for maximization**: using `mid = (lo+hi)//2` with `lo = mid` causes infinite loop when `lo+1 == hi`; use `(lo+hi+1)//2` instead.
- **Confusing array binary search with answer binary search**: you're not searching `nums` — you're searching the answer range. The feasibility check scans `nums`.
- **Feasibility check direction**: for minimization, `feasible(mid)` means "mid is good enough, try smaller" → `hi = mid`. Getting this backwards gives the wrong boundary.
- **Integer vs float**: `ceil(p / k)` requires `math.ceil` or `(p + k - 1) // k` for integer arithmetic — avoid float division for large inputs.
