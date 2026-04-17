# LeetCode Progress Log

One line per session: `[DATE] — [Pattern]: [Problem Title] (#N) — [one-sentence takeaway]`

---

## Existing Solutions (pre-system, mapped to patterns)

- `patterns/sliding-window/3_longest_substring_without_repeating_characters.py` — Sliding Window
- `patterns/dynamic-programming/5_longest_palindrome.py` — DP / Two Pointers (expand-around-center)
- `other/7_reversed_integer.py` — Math (no pattern)
- `other/8_string_to_signed_int.py` — Parsing / edge cases (no pattern)

---

## Sessions

<!-- New entries go here, most recent first -->
- 2026-04-17 — Dynamic Programming (1D): Coin Change (#322) — dp[i] = min(dp[i], dp[i-c]+1) for each coin; float('inf') initializes unreachable states, dp[0]=0 is the base case.
- 2026-04-17 — Dynamic Programming (1D): House Robber (#198) — dp[i] = max(nums[i] + dp[i-2], dp[i-1]); dp[i-1] carries full optimal history so you never need to track which houses were robbed.
- 2026-04-17 — Binary Search: Capacity To Ship Packages (#1011) — lo=max(weights) not 1; feasible greedily tracks remaining daily capacity and increments day count on overflow.
- 2026-04-17 — Binary Search: Koko Eating Bananas (#875) — search the answer space [1, max(piles)]; feasibility is just sum(ceil(p/k)) <= h; lo=1 not 0 since k is a divisor.
- 2026-04-16 — DFS/Backtracking: Subsets (#78) — record at every call (not just leaves); `i+1` for no-reuse; same three-line loop body as Combination Sum.
- 2026-04-16 — DFS/Backtracking: Combination Sum (#39) — choose/explore/unchoose: pass `i` to allow reuse, `path[:]` to snapshot, `pop()` to undo; the invariant is that `path` is always clean when entering a new branch.
- 2026-04-16 — BFS: Number of Islands (#200) — outer loop counts components, BFS flood-fills each island in-place; marking '0' on enqueue (not dequeue) is the key discipline.
- 2026-04-16 — BFS: Rotting Oranges (#994) — multi-source BFS seeds all rotten oranges at level 0; only increment minutes when a level actually converts new oranges to avoid off-by-one.
- 2026-04-13 — Two Pointers: Container With Most Water (#11) — always move the shorter wall; moving the taller one can only make things worse.
- 2026-04-13 — Sliding Window: Longest Repeating Character Replacement (#424) — window is invalid when `size - max_frequency > k`; the key is recognizing that replacements needed equals non-dominant characters in the window.
- 2026-04-13 — Two Pointers: 3Sum (#15) — fix one element in the outer loop, reduce to a two-pointer two-sum on the sorted remainder; skip duplicates at both the outer and inner levels.
