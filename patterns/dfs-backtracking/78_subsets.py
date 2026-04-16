from typing import List

# Pattern: Backtracking — generate all subsets (power set)
# Every call represents a valid subset — record at the top, not just at leaves.
# Pass i+1 (no reuse): each element used at most once.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(start, path, candidates):
            results.append(path[:])          # record every path, not just complete ones

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i + 1, path, candidates)   # i+1: no reuse
                path.pop()

        backtrack(0, [], nums)
        return results
