class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        longest = 0

        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[i])
            longest = max(longest, i - left + 1)
        return longest