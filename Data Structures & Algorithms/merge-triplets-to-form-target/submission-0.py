class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        x, y, z = target

        x_value = y_value = z_value = False

        for a, b, c in triplets:

            if a > x or b > y or c > z:
                continue

            if a == x:
                x_value = True
            if b == y:
                y_value = True
            if c == z:
                z_value = True

            if x_value and y_value and z_value:
                return True

        return x_value and y_value and z_value
                            
