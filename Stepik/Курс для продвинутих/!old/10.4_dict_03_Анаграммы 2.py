word1 = input().lower()
word2 = input().lower()

word1_dict = {letter: word1.count(letter) for letter in word1 if letter not in '. ,!?:;-'}
word2_dict = {letter: word2.count(letter) for letter in word2 if letter not in '. ,!?:;-'}

# word1_dict = {letter: word1.count(letter) for letter in word1}
# word2_dict = {letter: word2.count(letter) for letter in word2}

if word1_dict == word2_dict:
    print('YES')
else:
    print('NO')