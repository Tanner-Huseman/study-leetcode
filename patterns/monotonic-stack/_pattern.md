<!-- STATUS: complete -->
# Monotonic Stack

## The Concept
Use a monotonic stack when you need the next or previous greater/smaller element for each position. The stack acts as a "waiting room" of unresolved indices — when a new element arrives that breaks the monotonic property, it resolves all the waiting elements it dominates.

## The Template
```python
def monotonic_stack_template(nums):
    stack = []               # stores indices, not values — position info is usually needed
    result = [0] * len(nums) # default 0 (or -1) means "no answer found"

    for i, num in enumerate(nums):
        # while current element breaks the monotonic property (next-greater variant)
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = i - idx    # days to wait; or just num for "next greater value"

        stack.append(i)

    return result
    # indices remaining in stack have no next-greater element (result stays at default)
```

## When to Recognize It
- "Find the next greater / next smaller element for each position"
- "Find the previous greater / previous smaller element"
- "Calculate spans, widths, or areas involving the nearest boundary" (histogram, temperatures)
- O(n²) brute force is obvious but too slow — need O(n)
- Problem involves scanning left-to-right and needing the "most recent relevant" element

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|------------|-------------|
| 739 | Daily Temperatures | Medium | Stack holds unresolved indices (waiting room); pop and record `i - idx` when a warmer day arrives |
| 496 | Next Greater Element I | Medium | Pre-build `{value: index}` map for nums1; use `.get()` and `is not None` check to avoid index-0 falsy bug |

## Gotchas / Failure Modes
- Store **indices** in the stack, not values — you almost always need position to compute distance or map back to result
- Remaining indices in the stack after the loop are valid: they just have no answer (leave at default)
- For "next greater value" return the value; for "days until" return `i - idx` — same structure, different result assignment
- Decreasing monotonic stack → resolves on larger element (next-greater); increasing → resolves on smaller (next-smaller)
