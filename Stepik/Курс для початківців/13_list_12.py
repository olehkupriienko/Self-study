n = int(input())
nn = []
for i in range(1, n+1):
    nn.append(input())

p = []
for j in range(n-1):
    p.append(nn[j+1]+nn[j])
print(p)
