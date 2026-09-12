class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def backtrack(start, current, sum):

            if sum == target:
                result.append(current.copy())
                return

            if sum > target:
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i-1]:
                    continue

                current.append(candidates[i])

                backtrack(i + 1, current, sum + candidates[i])
                current.pop()

        candidates.sort()
        backtrack(0, [], 0)

        return result

            
