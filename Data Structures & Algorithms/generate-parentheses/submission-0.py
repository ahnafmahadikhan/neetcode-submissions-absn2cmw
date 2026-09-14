
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def backtrack(count, open_count, close_count):

            if len(count) == n * 2:
                result.append(count)
                return

            if open_count < n:
                backtrack(count + "(", open_count + 1, close_count)

            if close_count < open_count:
                backtrack(count + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result        
