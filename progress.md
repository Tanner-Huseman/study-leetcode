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
- 2026-04-16 — BFS: Rotting Oranges (#994) — multi-source BFS seeds all rotten oranges at level 0; only increment minutes when a level actually converts new oranges to avoid off-by-one.
- 2026-04-13 — Two Pointers: Container With Most Water (#11) — always move the shorter wall; moving the taller one can only make things worse.
- 2026-04-13 — Sliding Window: Longest Repeating Character Replacement (#424) — window is invalid when `size - max_frequency > k`; the key is recognizing that replacements needed equals non-dominant characters in the window.
- 2026-04-13 — Two Pointers: 3Sum (#15) — fix one element in the outer loop, reduce to a two-pointer two-sum on the sorted remainder; skip duplicates at both the outer and inner levels.
