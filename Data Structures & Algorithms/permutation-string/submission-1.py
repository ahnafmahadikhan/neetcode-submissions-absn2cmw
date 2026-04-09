class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        answer = 0
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False
        s1_count = Counter(s1)
        new_s2 = Counter(s2[0:len_s1])
        if Counter(s1_count) == Counter(new_s2):
            return True
        for i in range(len_s1,len_s2):
            first_char = s2[i-len_s1]
            end_char = s2[i]
            new_s2[first_char] -= 1
            if new_s2[first_char] == 0:
                del new_s2[first_char]
            new_s2[end_char] += 1
            if s1_count == new_s2:
                return True
        return False

