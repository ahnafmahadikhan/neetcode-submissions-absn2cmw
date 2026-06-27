import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxheap = [-x for x in nums]
        heapq.heapify(maxheap)

        for i in range(len(maxheap)) :
            if i == k - 1:
                return -heapq.heappop(maxheap)
            heapq.heappop(maxheap)
