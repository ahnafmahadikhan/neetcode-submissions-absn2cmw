class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = [0] * 26

        for i in tasks:
            count[ord(i) - ord('A')] += 1

        maxf = max(count)
        maxCount = 0

        for i in count:
            if i == maxf:
                maxCount += 1

        time = (maxf - 1) * (n + 1) + maxCount

        return max(time, len(tasks))