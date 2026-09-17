class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def new_rob(arr):
            
            if len(arr) == 1:
                return arr[0]

            dp = [0] * len(arr)

            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                dp[i] = max(dp[i - 1], arr[i] + dp[i - 2])

            return dp[len(arr) - 1]

        return max(new_rob(nums[1:n]), new_rob(nums[0:n - 1]))