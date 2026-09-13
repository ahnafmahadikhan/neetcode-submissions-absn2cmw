class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = set()

        def backtrack(current,start):
            
           
            result.add(tuple(current))

            for i in range(start, len(nums)):
                current.append(nums[i])

                backtrack(current, i + 1)
                current.pop()


        nums.sort()

        backtrack([],0)

        return [list(x) for x in result]