# LeetCode — Pattern-Focused Study System

## Goal

Pattern mastery for **Senior/Staff Data Platform Engineer** interviews at data-focused tech companies.
NOT FAANG grinding. NOT solving 300 problems. Learning reusable templates that solve 80% of what gets asked at target companies.

## The Template-First Philosophy

For each pattern, learn in this order:
1. **The template** — the skeleton Python code that solves the generic case, heavily annotated
2. **2-3 representative problems** — demonstrate the template and its common variants
3. **Failure modes** — when this pattern looks like it applies but doesn't

Depth over breadth. One well-understood pattern is worth more than ten half-learned ones.

## Pattern Priority

Ordered by interview frequency for target roles (data-focused, not pure SWE):

| Priority | Pattern | Status |
|----------|---------|--------|
| 1 | Sliding Window | Complete (3 problems) |
| 2 | Two Pointers | In progress (1 problem) |
| 3 | BFS (Graph traversal) | Not started |
| 4 | DFS / Backtracking | Not started |
| 5 | Binary Search (on answer) | Not started |
| 6 | Dynamic Programming (1D) | In progress (1 problem) |
| 7 | Heap / Priority Queue | Not started |
| 8 | Monotonic Stack | Not started |
| 9 | Union Find | Not started |
| 10 | Trie | Not started |

**Update this table after each session.**

## Folder Structure

```
patterns/
  [pattern-name]/
    _pattern.md        ← living reference doc (written by /study sessions)
    [problem].py       ← solution files
other/
  [problem].py         ← math, parsing, edge-case problems (not pattern-driven)
progress.md            ← running session log
```

## Session Target

~30 minutes per session. One pattern or one problem per session. Consistency over intensity.
When time is short: do the study portion, skip the guided solve, come back to the problem next session.

## Interview Context

Target companies are data-focused (PropTech, automotive, entertainment, FinTech). They want:
- Can you reason about algorithms clearly?
- Can you discuss time/space complexity without prompting?
- Can you handle Medium difficulty confidently?

Hard DP on trees and graph isomorphism are not the focus. Sliding window, two pointers, BFS/DFS, and binary search cover the vast majority of what gets asked.
