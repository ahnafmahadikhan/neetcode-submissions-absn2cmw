class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                right = i
                
                if stack:
                    left = stack[-1]
                else:
                    left = - 1

                w = i - left - 1
                area = h * w
                max_area = max(area, max_area)

            stack.append(i)

        return max_area
                

                    
            

