n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
del a[1:len(a):2]
print(a)
