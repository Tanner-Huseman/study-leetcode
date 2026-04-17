<!-- STATUS: complete -->
# Heap / Priority Queue

## The Concept
Use a heap when you need repeated access to the min or max element as the dataset changes dynamically. Core use case: "K best/worst/closest things" or "process next event by priority" — where sorting once isn't enough because the set evolves.

## The Template
```python
import heapq

def heap_template(nums, k):
    # Python only has min-heap. To simulate max-heap: negate values.
    heap = []

    for num in nums:
        heapq.heappush(heap, num)          # O(log n) push

        if len(heap) > k:                  # maintain fixed-size heap of k elements
            heapq.heappop(heap)            # O(log n) pop — removes smallest

    return heap[0]   # heap[0] is the kth largest (min of top-k)

# --- Max-heap pattern ---
# heapq.heappush(heap, -val)   # push negated
# -heapq.heappop(heap)         # pop and negate back

# --- Heapify from list (O(n) vs O(n log n) for n pushes) ---
# heapq.heapify(arr)           # transforms list in-place
```

## When to Recognize It
- "Find the K largest / K smallest / K closest" — fixed-size heap
- "Repeatedly process the next minimum or maximum" — streaming or event-driven
- "Merge K sorted lists/arrays" — min-heap on (value, list_index)
- The naive sort-then-slice is O(n log n) but you only need O(n log k)
- Problem involves a running median or dynamic ordering as elements arrive

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|------------|-------------|
| 215 | Kth Largest Element in an Array | Medium | Min-heap of size k: invariant is heap holds the k largest seen so far; heap[0] is the answer |

## Gotchas / Failure Modes
- Python's `heapq` is min-heap only — negate values to simulate max-heap
- Don't forget `import heapq`; it's not auto-imported even though it's stdlib
- Fixed-size heap pattern: push first, then pop if over k — not the other way around
- `heapq.heapify(arr)` is O(n); building via n pushes is O(n log n) — prefer heapify when you have the full list upfront
