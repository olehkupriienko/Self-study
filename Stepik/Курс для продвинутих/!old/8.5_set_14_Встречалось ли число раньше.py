numbers = [int(i) for i in input().split()]

numbers_set = set()

# for num in numbers:
#     old_len = len(numbers_set)
#     numbers_set.add(num)
#     new_len = len(numbers_set)
#     if new_len == old_len + 1:
#         print('NO')
#     else:
#         print('YES')


for num in numbers:
    if num in numbers_set:
        print('YES')
    else:
        print('NO')
    numbers_set.add(num)
