import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []

        for x, y in points:
            distance = -(x ** 2 + y ** 2)
            heapq.heappush(maxheap,[distance, x, y])

            while len(maxheap) > k:
                heapq.heappop(maxheap)
            
        answer = []
        while maxheap:
            distance, x, y = heapq.heappop(maxheap)
            answer.append([x, y])
        
        return answer