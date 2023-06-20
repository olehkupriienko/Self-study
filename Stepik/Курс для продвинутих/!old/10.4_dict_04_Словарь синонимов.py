n = int(input())

first_dict = {key: value for key, value in (input().split() for _ in range(n))}
second_dict = {key: value for value, key in first_dict.items()}

word = input()
if word in first_dict:
    print(first_dict[word])
elif word in second_dict:
    print(second_dict[word])

