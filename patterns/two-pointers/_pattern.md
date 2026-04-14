<!-- STATUS: complete -->
# Two Pointers

## The Concept
Eliminates O(n²) pair-checking by starting at both ends of a **sorted** array and converging inward. Because the array is sorted, moving one pointer is guaranteed to monotonically increase or decrease the current sum — so no valid pair is ever skipped.

## The Template
```python
def two_pointers(arr):
    arr.sort()                        # sorting is usually required
    left, right = 0, len(arr) - 1    # start at both ends

    while left < right:
        current = arr[left] + arr[right]

        if current == target:
            # record result
            left += 1
            right -= 1
            # skip duplicates after a match if needed:
            # while left < right and arr[left] == arr[left-1]: left += 1
            # while left < right and arr[right] == arr[right+1]: right += 1

        elif current < target:
            left += 1    # need larger sum — move left forward

        else:
            right -= 1   # need smaller sum — move right back

    return result
```

> Variant (same direction): both pointers start at index 0 and move forward at different speeds. Used for cycle detection or in-place partitioning (Dutch National Flag).

## When to Recognize It
- Array is sorted, or sorting is acceptable (returning values, not indices)
- Need to find pairs or triplets summing to a target
- "Two Sum", "3Sum", "closest to target", "container with most water"
- In-place duplicate removal or partitioning
- Brute force is O(n²) and obviously wasteful

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|------------|-------------|
| 15 | 3Sum | Medium | Fix `nums[i]` in outer loop, two-pointer on remaining subarray for `-nums[i]`; skip duplicates at both levels |

## Gotchas / Failure Modes
- **Forgot to sort**: two pointers are meaningless on unsorted input — always sort first unless the problem guarantees sorted order.
- **Duplicate triplets**: must skip at two levels — outer loop (`if i > 0 and nums[i] == nums[i-1]: continue`) AND inner loop after a match.
- **Bounds on inner skip loops**: `while jval == nums[j] and j < k` — without the bounds guard, you'll index out of range on arrays of all equal elements (e.g., `[0,0,0,0]`).
- **Wrong when indices matter**: if the problem asks for indices (classic Two Sum), a hash map is O(n) and correct; two pointers require sorting which destroys original indices.
- **3 variables ≠ 3 pointers**: fix one with the outer loop, reduce to two-pointer subproblem — don't try to move all three simultaneously.
