def check_points(x=0, y=0, z=None):
    if z is None:
        z = 0
    return x ** 2 + y ** 2 + z ** 2 <= 4


points = []
for _ in range(3):
    points.append([float(_) for _ in input().split()])
bool_result = all(map(check_points, points))
print(bool_result)
