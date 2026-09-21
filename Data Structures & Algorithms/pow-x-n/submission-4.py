class Solution:
    def myPow(self, x: float, n: int) -> float:

        result = 1
        power = abs(n)

        while power >0:
            if power % 2 == 1:
                result = result * x

            x = x * x
            power = power // 2
        
        if n < 0:
            return 1 / result
        
        return result
