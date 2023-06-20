from random import shuffle
# word1 = input()
word1 = 'пост'
word_list = list(word1)
shuffle(word_list)
word2 = ''.join(letter for letter in word_list)
print(word2)