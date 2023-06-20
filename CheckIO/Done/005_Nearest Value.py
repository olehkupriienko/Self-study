def nearest_value(values, one):
    return min(sorted(values), key=lambda a: abs(a-one))

result = []
one = 13
for i in {4, 7, 10, 11, 12, 14, 17}:
    result.append(abs(i - one))
print(result)
result = sorted(result)
print(result)

#print(nearest_value({4, 7, 10, 11, 12, 17}, 13))
