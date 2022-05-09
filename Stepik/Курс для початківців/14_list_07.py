n = int(input())
ll = []
for _ in range(n):
    ll.append(input())

k = int(input())
request = []
for _ in range(k):
    request.append(input().casefold())

for i in range(n):
    counter = 0
    for j in range(k):
        if request[j] in ll[i].casefold():
            counter += 1
    if counter == k:
        print(ll[i])
