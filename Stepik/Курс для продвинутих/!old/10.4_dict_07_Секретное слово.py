secret_word = input()
secret_word_dict = {}
for key in secret_word:
    secret_word_dict[key] = secret_word_dict.get(key, 0) + 1

numbers_of_letters = int(input())
decipher_dict = {}

for j in range(numbers_of_letters):
    value, key = tuple(input().split(': '))
    decipher_dict[int(key)] = value

for _ in secret_word:
    if secret_word_dict[_] in decipher_dict.keys():
        print(decipher_dict[secret_word_dict[_]], end='')

