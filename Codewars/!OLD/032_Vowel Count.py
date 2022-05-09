test = 'Incorrect answer for'

def vowel(text):
    vowel = 'aeiou'
    return len([i for i in text if i in vowel])


print(vowel(test))
