import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        new_stones = []
        for s in stones:
            new_stones.append(-s)

        stones = new_stones
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            two = heapq.heappop(stones)

            if first != two:
                heapq.heappush(stones, first - two)
            
        if stones:
            return -stones[0]
        else:
            return 0
    
