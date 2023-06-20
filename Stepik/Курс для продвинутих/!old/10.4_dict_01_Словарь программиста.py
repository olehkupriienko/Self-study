programmers_dict = {}

n = int(input())
for i in range(n):
    word, definition = input().split(': ')
    programmers_dict[word.lower()] = definition

m = int(input())
words_to_search = [input().lower() for __ in range(m)]

# for word in words_to_search:
#     if word in programmers_dict.keys():
#         print(f'{programmers_dict[word]}')
#     else:
#         print('Не найдено')

for _ in range(m):
    print(programmers_dict.get(words_to_search[_], 'Не найдено'))
