test = 'hello   world'


def backward_string_by_word(text: str) -> str:
    # your code here
    # res = [word[::-1] for word in text.split(' ')]

    return ' '.join(item for item in [word[::-1] for word in text.split(' ')])


print(backward_string_by_word(test))
