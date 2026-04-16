<!-- STATUS: in progress -->
# DFS / Backtracking

## The Concept
Backtracking explores all valid paths through a decision tree by making a choice, recursing deeper, then *undoing* the choice so the next branch starts from a clean slate. Used when you need every valid combination/permutation/path, not just one optimal answer.

## The Template
```python
def backtrack(start, path, result):
    # BASE CASE: path is complete — record a copy, not a reference
    if <path_is_complete>:
        result.append(path[:])   # path[:] snapshots current state; bare path mutates later
        return

    for i in range(start, len(candidates)):
        # PRUNE: skip branches that can't lead to a valid answer
        if <invalid_choice>:
            continue

        # CHOOSE
        path.append(candidates[i])

        # EXPLORE
        # pass i     → allows reuse of candidates[i] (unlimited picks)
        # pass i+1   → no reuse (each element used at most once)
        backtrack(i, path, result)

        # UNCHOOSE — restore path to pre-choice state
        path.pop()
```

## When to Recognize It
- "Find **all** combinations / permutations / subsets" — output is `List[List[int]]`
- The word "generate" in the problem title
- "Is there **any** path through this grid satisfying X?" (word search, maze)
- Brute force enumerates everything; most branches can be discarded early
- Optimal substructure is NOT required — you need every answer, not the best one

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|------------|-------------|
| 39 | Combination Sum | Medium | Pass `i` (not `i+1`) to allow reuse; `remaining < 0` prunes over-target branches; `path[:]` copies on record |

## Gotchas / Failure Modes
- **Forgot `path[:]` on append** — storing a bare reference means every recorded result points to the same list, which will be empty when the recursion fully unwinds.
- **`i` vs `i+1`**: this single character decides whether reuse is allowed — get it wrong and you either miss solutions or generate duplicates.
- **Statements as expressions** — `path.append()` returns `None`; `remaining -= x` is a statement. Both break if used inline as function arguments. Always write choose/explore/unchoose as three separate lines.
- **When NOT to use** — if you only need one valid answer (not all), DFS with early return is enough and backtracking overhead is wasted. If you need the *optimal* answer, DP is usually better.
