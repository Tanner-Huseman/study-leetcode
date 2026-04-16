<!-- STATUS: in progress -->
# BFS (Breadth-First Search)

## The Concept
BFS explores nodes level by level from one or more sources, guaranteeing the first time a node is reached it's via the shortest path. A queue enforces FIFO order — all distance-1 neighbors are fully processed before any distance-2 neighbor is touched.

## The Template
```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}       # add to visited BEFORE enqueuing, not after dequeuing

    distance = 0

    while queue:
        # snapshot current level size — process all nodes at this distance
        for _ in range(len(queue)):
            node = queue.popleft()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)   # mark here to avoid duplicate enqueues
                    queue.append(neighbor)

        distance += 1       # every node just processed was `distance` hops away

    return distance
```

**Grid variant** — replace `graph[node]` with 4-directional neighbors:
```python
for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
        visited.add((nr, nc))
        queue.append((nr, nc))
```

**Multi-source BFS** — seed the queue with *all* starting nodes before the loop. All sources are treated as distance 0; the level counter advances correctly from there.

**Off-by-one guard** — increment distance (or minutes) only when a level actually enqueues new nodes:
```python
if added_this_level:
    minutes += 1
```
Otherwise the last "empty" level fires an extra increment.

## When to Recognize It
- "Minimum steps / shortest path / minimum time to reach X"
- Spread or infection propagating outward from one or more sources simultaneously
- Grid problems: "nearest", "closest", "how many steps"
- "How many levels until condition Y?" — DFS gives *a* path, not the *shortest* one
- Unweighted graph; if edges have weights, use Dijkstra instead

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|------------|-------------|
| 994 | Rotting Oranges | Medium | Multi-source BFS from all rotten oranges at once; `rotten_oranges` set doubles as visited; count fresh up front and decrement to detect impossible case |

## Gotchas / Failure Modes
- **Mark visited on enqueue, not dequeue** — marking on dequeue allows the same node to be enqueued multiple times, causing duplicate work or wrong counts.
- **Multi-source setup** — seed ALL sources into the queue before starting; don't BFS from each source independently (that gives wrong minimum times).
- **Off-by-one on level counter** — the last BFS level processes nodes but enqueues nothing; if you increment unconditionally, you overshoot by 1. Guard with `if added_this_level`.
- **Impossible case** — BFS completing doesn't mean all nodes were reached; always verify post-loop (e.g., `if fresh_oranges > 0: return -1`).
- **When NOT to use** — if edge weights vary, BFS gives wrong shortest paths; use Dijkstra (min-heap). If you need *all* paths or want to explore deeply before backtracking, DFS is more natural.
