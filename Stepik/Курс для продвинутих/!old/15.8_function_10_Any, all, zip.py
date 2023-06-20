abscissas = [float(_) for _ in input().split()]  # x
ordinates = [float(_) for _ in input().split()]  # y
applicates = [float(_) for _ in input().split()]  #z

result = all(map(lambda point: point[0]**2 + point[1]**2 + point[2]**2 <= 4, zip(abscissas, ordinates, applicates)))
print(result)


result2 = all(x**2 + y**2 + z**2 <= 4 for x, y, z in zip(abscissas, ordinates, applicates))
print(result2)


result3 = all(map(lambda x, y, z: x**2 + y**2 + z**2 <= 4, abscissas, ordinates, applicates))
print(result3)