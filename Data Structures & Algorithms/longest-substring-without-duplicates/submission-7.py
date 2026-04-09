class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqe_char = set()
        longest = 0
        left = 0
        
        for i in range(len(s)):
            while s[i] in uniqe_char:
                uniqe_char.remove(s[left])
                left += 1
            uniqe_char.add(s[i])
            longest = max(longest, i - left + 1)
        return longest
