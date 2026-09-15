class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        result = []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }


        def backtrack(start, current):

            if start == len(digits):
                result.append("".join(current))
                return

            letters = phone[digits[start]]

            for letter in letters:
                current.append(letter)

                backtrack(start + 1, current)

                current.pop()
            


        backtrack(0, [])

        return result