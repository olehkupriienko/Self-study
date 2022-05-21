arr = 'a b v'.split()

result = [[]]
for i in range(len(arr)):
    for j in range(i+1, len(arr)+1):
        result.append(arr[i:j])
result.sort(key=lambda x: len(x))
print(result)
