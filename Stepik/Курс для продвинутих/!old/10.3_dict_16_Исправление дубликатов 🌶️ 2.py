# test = input()
test = 'a b c a a d c'

def postfix_duplicates(line):
    letters_dict = {}
    result = []
    for letter in line.split():
        letters_dict[letter] = letters_dict.get(letter, -1) + 1
        if letters_dict[letter] == 0:
            result.append(letter)
        else:
            result.append(letter + "_" + str(letters_dict[letter]))
    return ' '.join(result)



print(postfix_duplicates(test))