from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        most_freq = Counter(nums).most_common(k)
        result = []

        for i in most_freq:
            result.append(i[0])

        return result