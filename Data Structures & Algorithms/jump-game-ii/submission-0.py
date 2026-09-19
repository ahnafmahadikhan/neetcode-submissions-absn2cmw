class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        answer = 0
        maximum = 0
        currnet_end = 0

        for i in range(len(nums) - 1):

            maximum = max(maximum, i + nums[i])

            if i == currnet_end:
                answer += 1
                currnet_end = maximum

            if currnet_end >= len(nums) - 1:
                break

        return answer
