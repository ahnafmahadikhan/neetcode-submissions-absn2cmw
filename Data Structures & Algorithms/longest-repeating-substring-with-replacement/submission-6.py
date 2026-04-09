class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        answer = 0
        left = 0
        max_length = 0

        for i in range(len(s)):
            count[s[i]] += 1
            max_length = max(max_length, count[s[i]])

            while (i - left + 1) - max_length > k:
                count[s[left]] -= 1
                left += 1
            answer = max(answer, i - left + 1)
        
        return answer