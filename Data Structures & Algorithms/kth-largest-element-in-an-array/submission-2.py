import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        new_nums = []

        for x in nums:
            new_nums.append(-x)

        heapq.heapify(new_nums)

        for x in range(len(new_nums)):
            if x == k-1:
                return -heapq.heappop(new_nums)
            
            heapq.heappop(new_nums)