from typing import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count_s1 = Counter(s1)
        count_s2 = Counter(s2[0 : len(s1)])

        if len(s1) > len(s2):
            return False

        if count_s1 == count_s2:
            return True

        for i in range(len(s1),len(s2)):

            first_char = s2[i - len(s1)]
            end_char = s2[i]

            count_s2[first_char] -= 1
            
            if count_s2[first_char] == 0:
                del count_s2[first_char]

            count_s2[end_char] += 1

            if count_s1 == count_s2:
                return True

        return False
             


