class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = set(nums)
        max_length = 0
        
        for i in answer:
            if i - 1 not in answer:
                lenght = 1
                while i + lenght in answer:
                    lenght += 1
                max_length = max(max_length, lenght)
                
        return max_length