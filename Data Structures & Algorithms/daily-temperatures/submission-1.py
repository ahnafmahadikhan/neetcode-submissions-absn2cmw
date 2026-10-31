class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                top = stack.pop()
                result[top] = i - top
            stack.append(i)
        
        return result