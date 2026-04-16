from collections import deque
from typing import List

# Pattern: Multi-source BFS
# Seed all rotten oranges into the queue at level 0.
# Each BFS level = 1 minute of rotting.
# Guard the minute increment so the final empty level doesn't overshoot.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0
        rotten_oranges = set()

        if not grid:
            return -1

        row_count = len(grid)
        col_count = len(grid[0])

        # Scan grid: collect all rotten sources, count fresh oranges
        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 2:
                    rotten_oranges.add((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Multi-source BFS: all rotten oranges start at minute 0
        queue = deque(list(rotten_oranges))
        minutes = 0

        neighbors = [
            (0, 1),   # right
            (1, 0),   # down
            (0, -1),  # left
            (-1, 0),  # up
        ]

        while queue:
            level_len = len(queue)
            added_to_queue = False

            for _ in range(level_len):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < row_count and 0 <= nc < col_count
                            and (nr, nc) not in rotten_oranges
                            and grid[nr][nc] == 1):
                        queue.append((nr, nc))
                        rotten_oranges.add((nr, nc))  # visited on enqueue
                        added_to_queue = True
                        fresh_oranges -= 1

            # Only count this level as a minute if new oranges actually rotted
            if added_to_queue:
                minutes += 1

        # If any fresh oranges remain, they were unreachable
        if fresh_oranges == 0:
            return minutes
        return -1
