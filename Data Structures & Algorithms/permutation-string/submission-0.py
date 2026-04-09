from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        for i in range(len_s2 - len_s1 + 1):
            sx = s2[i:i + len_s1]

            if Counter(sx) == Counter(s1):
                return True

        return False