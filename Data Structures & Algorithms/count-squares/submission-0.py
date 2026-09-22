class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        
        point = tuple(point)

        if point  in self.points:
            self.points[point] += 1
        else:
            self.points[point] = 1

    def count(self, point: List[int]) -> int:
        
        res = 0
        x, y = point

        for (px, py), freq in self.points.items():

            if px == x or py == y:
                continue
            if abs(px - x) != abs(py - y):
                continue

            point1 = (px, y)
            point2 = (x, py)

            if point1 in self.points and point2 in self.points:
                res += freq * self.points[point1] * self.points[point2]

        return res
