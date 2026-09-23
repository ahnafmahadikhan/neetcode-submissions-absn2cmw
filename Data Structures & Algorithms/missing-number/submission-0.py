class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n + 1):

            nums.append(i)

        result = 0

        for i in range (n * 2 + 1):

            result = result ^ nums[i]

        return result