class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        from typing import List

        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        for position, speed in cars:
            times = (target - position) / speed
            if not stack or times > stack[-1]:
                stack.append(times)
        
        return len(stack)