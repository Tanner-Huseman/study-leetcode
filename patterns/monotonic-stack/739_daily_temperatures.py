from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Monotonic stack (decreasing). Stack is a waiting room of unresolved indices.
        When a warmer day arrives, pop everything colder and record the wait.

        Time: O(n) — each index pushed and popped at most once
        Space: O(n) — stack + result
        """
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)

        return result
