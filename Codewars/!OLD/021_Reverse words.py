test = 'The quick brown fox jumps over the lazy dog.'


def reverse_words(text):
    return ' '.join([i[::-1] for i in text.split()])

def reverse_words2(text):
    result = text.split(' ')
    for i in range(len(result)):
        result[i] = result[i][::-1]

    return (' '.join(result))


print(reverse_words(test))
