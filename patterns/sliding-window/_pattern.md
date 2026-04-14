<!-- STATUS: complete -->
# Sliding Window

## The Concept
Maintains a variable-size window `[left, right]` over a sequence, expanding right on each iteration and shrinking left only when the window becomes invalid. Avoids O(n²) recomputation by never re-examining elements behind the left boundary.

## The Template
```python
def sliding_window(s):
    left = 0
    window = {}        # tracks state of current window — char counts, sum, etc.
    answer = 0

    for right in range(len(s)):
        # EXPAND: add s[right] into the window
        window[s[right]] = window.get(s[right], 0) + 1

        # SHRINK: while window is invalid, remove s[left] and advance
        while <window_is_invalid>:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        # RECORD: window [left..right] is now valid
        answer = max(answer, right - left + 1)

    return answer
```

## When to Recognize It
- "Longest/shortest subarray or substring satisfying X"
- Fixed-size window: "max sum of subarray of size k"
- Constraint on window contents: at most k distinct chars, no repeats, sum ≤ limit
- Brute force would be O(n²) nested loops over start/end
- Window validity degrades monotonically as it grows (shrinking left never needs revisiting)

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|------------|-------------|
| 3 | Longest Substring Without Repeating Characters | Medium | Window invalid when any char count > 1; shrink until no duplicates |
| 424 | Longest Repeating Character Replacement | Medium | Replacements needed = `window_size - max_frequency`; shrink when that exceeds k |

## Gotchas / Failure Modes
- **Validity condition**: defining what makes a window invalid is the whole problem — get that wrong and everything else follows incorrectly.
- **`max(window.values())` is O(alphabet size)**, not O(n) — fine for uppercase letters (26), but track a running max variable for large alphabets.
- **Off-by-one on window size**: `right - left + 1`, not `right - left`.
- **When NOT to use**: if you need the optimal subarray but the validity condition isn't monotonic (e.g., shrinking the window could make it valid again in a non-trivial way), sliding window breaks down.
- **Fixed vs. variable window**: fixed-size problems (exactly k elements) don't need a `while` shrink — just check if `right >= k` and remove `s[right - k]`.
