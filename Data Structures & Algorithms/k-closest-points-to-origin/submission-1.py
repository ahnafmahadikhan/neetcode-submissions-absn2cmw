import heapq
from typing import List
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        answer = []
        
        for x, y in points:
            distance = -(x**2 + y**2)
            heapq.heappush(answer, [distance, x, y])

        while len(answer) > k:
            heapq.heappop(answer)

        f_answer = []

        while answer:

            distance, x, y = heapq.heappop(answer)
            f_answer.append([x, y])

        return f_answer

        
        

        

        