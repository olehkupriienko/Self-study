test = "The quick, brown fox jumps over the lazy dog!"


def is_pangram(s):
    alfabet = ''
    for i in s.lower():
        if i.isalpha() and i not in alfabet:
            alfabet += i
    return len(alfabet) == 26


print(is_pangram(test))