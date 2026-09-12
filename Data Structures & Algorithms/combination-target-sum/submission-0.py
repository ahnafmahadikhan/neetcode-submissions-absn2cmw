from unittest import result


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start, sum, current):

            if sum == target:
                result.append(current.copy())
                return

            if sum > target:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])

                backtrack(i, sum + nums[i], current)

                current.pop()

        backtrack(0, 0, [])

        return result   
        