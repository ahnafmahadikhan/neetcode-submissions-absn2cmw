class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in answer :
                return [answer[diff], i + 1]
            answer[num] = i + 1 