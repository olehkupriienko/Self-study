n = int(input())

phone_book = {}
for i in range(n):
    phone, name = input().lower().split()
    phone_book.setdefault(name, []).append(phone)

m = int(input())
name_to_find = [input().lower() for _ in range(m)]

for name in name_to_find:
    print(*phone_book.get(name, ['абонент не найден']))

# for name in name_to_find:
#     if name in phone_book:
#         print(' '.join(phone_book[name]))
#     else:
#         print('абонент не найден')
