# test = input()
test = 'a b c a a d c'


def postfix_duplicates(line):
    letters_dict = {}
    result = ''
    for letter in line.split():
        letters_dict[letter] = letters_dict.get(letter, -1) + 1
        if letters_dict[letter] == 0:
            result += letter + ' '
        else:
            result += letter + "_" + str(letters_dict[letter]) + ' '

    return result.strip()


print(postfix_duplicates(test))
