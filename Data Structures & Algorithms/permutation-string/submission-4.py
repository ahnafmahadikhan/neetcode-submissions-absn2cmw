class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s2 < len_s1:
            return False
        window_s2 = Counter(s2[0:len_s1])
        count_s1 = Counter(s1)
        if count_s1 == window_s2:
            return True

        for i in range(len_s1,len_s2):
            first_char = s2[i-len_s1]
            end_char = s2[i]
            window_s2[first_char] -= 1
            if window_s2[first_char] == 0:
                del window_s2[first_char]
            window_s2[end_char] += 1
            if count_s1 == window_s2:
                return True
        
        return False
