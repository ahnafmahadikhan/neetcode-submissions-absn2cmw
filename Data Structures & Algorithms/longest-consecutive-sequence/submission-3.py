class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uninum = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in uninum:
                lengthx = 1
                while num + lengthx in uninum:
                    lengthx = lengthx + 1
                longest = max(longest, lengthx)
        return longest
