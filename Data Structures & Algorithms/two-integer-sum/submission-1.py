class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from typing import List
        answer = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in answer :
                return [answer[diff], i]
            answer[num] = i
        