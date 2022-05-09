L = input().split()
M = input().split()

LM = []
for i in range(len(L)):
    LM.append(int(L[i])+int(M[i]))
print(*LM)
