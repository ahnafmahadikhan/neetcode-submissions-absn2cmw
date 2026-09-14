class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []

        def backtrack(start, current):

            if start == len(s):
                result.append(current.copy())
                return

            for i in range(start, len(s)):
                substring = s[start:i + 1]

                if substring == substring[::-1]:
                    current.append(substring)
                    
                    backtrack(i + 1, current)

                    current.pop()

        backtrack(0, [])
    
        return result