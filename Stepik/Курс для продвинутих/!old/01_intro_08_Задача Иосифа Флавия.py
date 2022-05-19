def joseph(n, k):
    return 1 if n == 1 else (joseph(n - 1, k) + k - 1) % n + 1

print(joseph(int(input()), int(input())))