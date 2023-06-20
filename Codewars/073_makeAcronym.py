test = 'My aunt sally'


def make_acronym(phrase: str):
    if not isinstance(phrase, str):
        return f'Not a string'
    elif not phrase.replace(' ', '').isalpha() or phrase.replace(' ', '').isdigit():
        return f'Not letters'
    else:
        return ''.join(i[0] for i in phrase.upper().split())


# print(test.replace(' ', '').isalnum())
print(make_acronym(test))
