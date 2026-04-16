from collections import deque
from typing import List

# Pattern: BFS flood fill — count connected components
# Outer loop finds each unvisited '1' (new island) and launches a BFS.
# BFS marks every reachable land cell '0' in-place (visited-on-enqueue),
# so the outer loop never counts the same island twice.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_tracker = 0
        if not grid:
            return island_tracker

        row_count = len(grid)
        col_count = len(grid[0])
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == '1':
                    island_tracker += 1
                    queue = deque([(r, c)])
                    grid[r][c] = '0'    # mark on enqueue, not on dequeue

                    while queue:
                        cr, cc = queue.popleft()

                        for dr, dc in neighbors:
                            nr, nc = cr + dr, cc + dc
                            if (0 <= nr < row_count and 0 <= nc < col_count
                                    and grid[nr][nc] == '1'):
                                queue.append((nr, nc))
                                grid[nr][nc] = '0'  # mark on enqueue

        return island_tracker
