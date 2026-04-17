import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Min-heap of size k. Invariant: heap holds the k largest elements seen so far.
        heap[0] is the smallest of those — i.e., the kth largest overall.

        Time: O(n log k)
        Space: O(k)
        """
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
