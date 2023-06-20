class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_between_points(a, b):
    return (abs(a.x - b.x)**2 + abs(a.y - b.y)**2)**0.5


print(distance_between_points(Point(3, 3), Point(3, 4)))
