class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        stack = []
        cars = sorted(zip(position, speed), reverse = True) 
    
        for p, s in cars:
            time = (target - p) / s

            if not stack or stack[-1] < time:
                stack.append(time)
                
        return len(stack)
