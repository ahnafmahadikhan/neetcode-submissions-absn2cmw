class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        count = defaultdict(int)
        left = 0
        max_count = 0

        for i in range(len(s)):
            count[s[i]] += 1
            max_count = max(max_count, count[s[i]])
            while (i - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            answer = max(i - left + 1, answer)
        return answer