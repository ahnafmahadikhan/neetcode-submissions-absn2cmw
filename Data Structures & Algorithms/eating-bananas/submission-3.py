from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid = (right + left) // 2
            hours = 0

            for p in piles:
                hours += ceil(p / mid)

            if hours <= h:
                result = mid
                right = mid - 1

            else:
                left = mid + 1

        return result 

