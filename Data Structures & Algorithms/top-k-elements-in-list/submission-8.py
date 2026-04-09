class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        from collections import Counter
        max_freq = Counter(nums).most_common(k)
        for num in max_freq:
            answer.append(num[0])
        return answer