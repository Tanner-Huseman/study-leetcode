from typing import List

# Pattern: Backtracking — find all combinations summing to target
# Key: pass i (not i+1) to allow reuse of the same candidate.
# Invariant: path holds exactly the choices made so far; pop() restores it after each branch.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])   # copy — not a reference
                return
            if remaining < 0:
                return                   # prune: over target

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  # i allows reuse
                path.pop()

        backtrack(0, [], target)
        return result
