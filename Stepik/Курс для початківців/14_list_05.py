n = int(input())
ll = []
for _ in range(n):
    ll.append(input())
request = input().lower()
for _ in range(n):
    if request in ll[_].lower():
        print(ll[_])
