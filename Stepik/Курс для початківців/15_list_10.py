palindromes1 = []

for i in range(100, 1001):
    if i // 100 == i % 10:
        palindromes1.append(i)

palindromes2 = [i for i in range(100, 1000) if i // 100 == i % 10]
palindromes3 = [i for i in range(100, 1000) if str(i)[0] == str(i)[-1]]


print(palindromes1)
print(palindromes2)
print(palindromes3)
