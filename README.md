# LeetCode — Pattern-Based Study System

A structured algorithm study system focused on reusable patterns, not grinding individual problems. Built to prepare for Senior/Staff Data Platform Engineer interviews.

## Philosophy

Learn templates, not solutions. Each pattern directory contains a `_pattern.md` — a living reference doc with the annotated template, recognition signals, and worked examples. These are built up progressively through `/study` sessions.

## Structure

```
patterns/
  sliding-window/      # Variable/fixed window on arrays or strings
  two-pointers/        # Left/right pointers, fast/slow pointers
  bfs/                 # Level-order traversal, shortest path
  dfs/                 # Tree/graph depth traversal, backtracking
  dynamic-programming/ # Optimal substructure problems
  binary-search/       # Search on sorted arrays AND on answer space
  heap-priority-queue/ # Top-K, median, scheduling problems
  monotonic-stack/     # Next greater/smaller element problems
  backtracking/        # Combinatorics, permutations, constraint satisfaction
  union-find/          # Connected components, cycle detection
  trie/                # Prefix matching, autocomplete
other/
  # Math, parsing, and edge-case problems that don't fit a pattern type
progress.md            # Running session log
```

## Usage

Start a study session from this repo:

```
/study                    # Claude picks the next pattern to work on
/study sliding-window     # Work on a specific pattern
```

## Pattern Priority

Tier 1 (highest interview frequency): Sliding Window, Two Pointers, BFS/DFS, Binary Search  
Tier 2: Heap, DP (1D), Monotonic Stack  
Tier 3: Backtracking, Union Find, Trie
