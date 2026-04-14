class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        maxarea = 0

        for i in range(len(heights)):
            
            while stack and heights[i] < heights[stack[-1]]:
               
                h = heights[stack.pop()]
                
                right = i
                
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                
                width = right - left -1
                
                area = h * width

                maxarea = max(maxarea, area)

            stack.append(i)

        return maxarea