class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = 0
        
        maximum_sum = float('-inf')

        for i in range(len(nums)):

            current_sum = max(nums[i], current_sum + nums[i])

            maximum_sum = max(maximum_sum, current_sum)

        return maximum_sum