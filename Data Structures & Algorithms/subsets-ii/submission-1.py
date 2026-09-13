class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(current,start):
            
           
            result.append(current.copy())

            for i in range(start, len(nums)):

                if i > start and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                backtrack(current, i + 1)
                
                current.pop()


        nums.sort()

        backtrack([],0)

        return result