count = 0

for a in range(1, 35):
    for b in range(a, 35):
        for c in range(1, 35):
            for d in range(c, 35):
                if a != b and a != c and a != d and b != c and b != d and c != d and ((a**3 + b**3) == (c**3 + d**3)):
                    print(a, b, c, d)
                    print(a**3 + b**3)
                    count += 1
                    if count == 5:
                        break
