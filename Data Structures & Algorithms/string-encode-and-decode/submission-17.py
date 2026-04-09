class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + "#" + i
        return s

    def decode(self, s: str) -> List[str]:
        answer = []
        left, right = 0, len(s) - 1
        while left < right:
            j = left
            while s[j] != "#":
                j += 1
            length = int(s[left:j])
            answer.append(s[j+1:j+1+length])
            left = j+1+length
        return answer